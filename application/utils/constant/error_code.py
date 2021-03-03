"""
ErrorEnum
"""
from enum import Enum


class ErrorEnum(Enum):
    """
    ErrorEnum, the name should follow the pattern {ENTITY}_{ERROR_CODE}_{DESCRIPTION}
    """
    # Auth
    AUTH_401_JWT = "auth_401_jwt"
    AUTH_401_SCOPE = "auth_401_scope"
    AUTH_500_SERVER = "auth_500_server"
