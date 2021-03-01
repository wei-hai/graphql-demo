"""
This module provides function to create Sanic application
"""

import sentry_sdk
from graphql.execution.executors.asyncio import AsyncioExecutor
from sanic import Sanic
from sanic_graphql import GraphQLView
from sentry_sdk.integrations.aiohttp import AioHttpIntegration
from sentry_sdk.integrations.logging import LoggingIntegration
from sentry_sdk.integrations.sanic import SanicIntegration
from sentry_sdk.integrations.sqlalchemy import SqlalchemyIntegration

from application.graphql.schema import schema
from application.services.common.db_client import AsyncDatabaseClient, AsyncEngineManager


async def before_server_start(app: Sanic):
    """
    Before server start
    @param app:
    @return:
    """
    is_development = app.config["ENV"] == "development"
    # Database
    AsyncEngineManager.create_engines(
        primary_database_urls=[app.config["PRIMARY_DATABASE_URL"]],
        replica_database_urls=[app.config["REPLICA_DATABASE_URL"]]
    )
    app.db_client = AsyncDatabaseClient()
    if not is_development:
        sentry_sdk.init(
            dsn=app.config["SENTRY_DSN"],
            environment=app.config["ENV"],
            integrations=[
                SanicIntegration(),
                AioHttpIntegration(),
                SqlalchemyIntegration(),
                LoggingIntegration(),
            ],
        )


async def after_server_stop(app: Sanic):
    """
    After server stop
    @param app:
    @return:
    """
    await AsyncEngineManager.close()


def create_app(default_settings: str = "application/settings/env.py") -> Sanic:
    """
    Create instance
    @param default_settings:
    @return:
    """
    app = Sanic(__name__)
    app.update_config(default_settings)

    @app.listener("before_server_start")
    async def _before_server_start(_app, loop):
        app.add_route(
            GraphQLView.as_view(
                schema=schema,
                graphiql=_app.config["ENV"] != "production",
                executor=AsyncioExecutor(loop=loop),
            ),
            "/graphql"
        )
        await before_server_start(_app)

    @app.listener("after_server_stop")
    async def _after_server_stop(_app, loop):
        await after_server_stop(_app)

    return app
