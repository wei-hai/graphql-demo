from enum import Enum


class ErrorEnum(Enum):
    # Auth
    AUTH_401_JWT = "auth_401_jwt"
    AUTH_401_SCOPE = "auth_401_scope"
    AUTH_500_SERVER = "auth_500_server"
