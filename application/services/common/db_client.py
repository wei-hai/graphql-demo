"""
AsyncDatabaseClient
"""

import random
from typing import List

from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker


class AsyncEngineManager:
    primary_engines: List[Engine] = []
    replica_engines: List[Engine] = []

    @staticmethod
    def create_engines(primary_database_urls: List[str], replica_database_urls: List[str]):
        for url in primary_database_urls:
            AsyncEngineManager.primary_engines.append(create_async_engine(url, echo=False))
        for url in replica_database_urls:
            AsyncEngineManager.replica_engines.append(create_async_engine(url, echo=False))

    @staticmethod
    async def close():
        for engine in AsyncEngineManager.primary_engines:
            await engine.dispose()
        for engine in AsyncEngineManager.replica_engines:
            await engine.dispose()


class AsyncDatabaseClient:
    """
    AsyncDatabaseClient
    """

    def __init__(self):
        """
        Init
        """
        self.primary_sessions = [sessionmaker(engine, expire_on_commit=False, class_=AsyncSession) for engine in
                                 AsyncEngineManager.primary_engines]
        self.replica_sessions = [sessionmaker(engine, expire_on_commit=False, class_=AsyncSession) for engine in
                                 AsyncEngineManager.replica_engines]
        self.primary_len = len(self.primary_sessions)
        self.replica_len = len(self.replica_sessions)

    def primary_session(self):
        return self.primary_sessions[random.randrange(self.primary_len)]()

    def replica_session(self):
        return self.replica_sessions[random.randrange(self.replica_len)]()
