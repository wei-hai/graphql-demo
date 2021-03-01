"""
This module includes functions to do authentication.
"""

import logging
import time
from functools import wraps
from typing import Callable, List

import jwt
from sanic.exceptions import Unauthorized
from sanic.request import Request

from application.utils.constant.error_code import ErrorEnum
from application.utils.constant.scope import ScopeEnum, ROLE_SCOPES

logger = logging.getLogger(__name__)


def generate_jwt(
        service_name: str,
        user_id: str,
        roles: List[str],
        secret: str,
        expiration: int,
) -> str:
    """
    Generate JWT
    @param service_name:
    @param user_id:
    @param roles:
    @param secret:
    @param expiration:
    @return:
    """
    now: int = int(time.time())
    payload: dict = {
        "iss": service_name,
        "sub": user_id,
        "roles": roles,
        "exp": now + expiration,
        "iat": now,
        "nbf": now,
    }
    return jwt.encode(payload, secret).decode()


def authenticate(request: Request, secret_key: str):
    """
    Authenticate jwt against secret in config
    @param request:
    @param secret_key:
    @return:
    """
    # In graphql request this call may execute multiple times,
    # we need to do authentication against secret_key only once
    if hasattr(request.ctx, secret_key):
        return
    if request.token is None:
        raise Unauthorized(ErrorEnum.AUTH_401_JWT.value)
    try:
        payload = jwt.decode(
            request.token, request.app.config[secret_key], algorithms=["HS256"], options=dict(require_exp=True)
        )
    except (
            jwt.ExpiredSignatureError,
            jwt.DecodeError,
            jwt.MissingRequiredClaimError,
    ) as ex:
        raise Unauthorized(ErrorEnum.AUTH_401_JWT.value) from ex
    scopes = frozenset()
    for role in request.ctx.roles:
        if role in ROLE_SCOPES:
            scopes = scopes.union(ROLE_SCOPES[role])
    request.ctx.scopes = scopes
    setattr(request.ctx, secret_key, True)
    request.ctx.user_id = payload["sub"]
    request.ctx.roles = payload["roles"]
    request.ctx.scopes = scopes


def authorize(request: Request, scope: ScopeEnum):
    """
    Authorize against user's scope
    :param request:
    :param scope:
    :return:
    """
    if scope not in request.ctx.scopes:
        raise Unauthorized(ErrorEnum.AUTH_401_SCOPE.value)


def auth(scope: ScopeEnum) -> Callable:
    """
    Decorator to do authentication against jwt secret and authorization against scope.
    @param scope:
    @return:
    """

    def auth_decorator(fn):
        @wraps(fn)
        async def wrapper(root, info, *args, **kwargs):
            request = info.context["request"]
            authenticate(request, "JWT_SECRET")
            authorize(request, scope)
            return await fn(root, info, *args, **kwargs)

        return wrapper

    return auth_decorator


def auth_refresh_jwt() -> Callable:
    """
    Decorator to do authentication against jwt refresh secret
    @return:
    """

    def auth_decorator(fn):
        @wraps(fn)
        async def wrapper(root, info, *args, **kwargs):
            request = info.context["request"]
            authenticate(request, "JWT_REFRESH_SECRET")
            return await fn(root, info, *args, **kwargs)

        return wrapper

    return auth_decorator
