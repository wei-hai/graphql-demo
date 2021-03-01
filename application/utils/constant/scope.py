from enum import Enum
from application.utils.constant.role import RoleEnum


class ScopeEnum(Enum):
    ORGANIZATION_READ = "organization:read"
    ORGANIZATION_WRITE = "organization:write"
    USER_READ = "user:read"
    USER_WRITE = "user:write"
    ROLE_READ = "role:read"
    ROLE_WRITE = "role:write"


USER_SCOPES = frozenset({
    ScopeEnum.ORGANIZATION_READ,
    ScopeEnum.USER_READ,
    ScopeEnum.ROLE_READ
})

ADMIN_SCOPES = frozenset(USER_SCOPES.union({
    ScopeEnum.ORGANIZATION_WRITE,
    ScopeEnum.USER_WRITE,
    ScopeEnum.ROLE_WRITE
}))

SUPER_ADMIN_SCOPES = frozenset(ADMIN_SCOPES.union({}))

EMPLOYEE_SCOPES = frozenset({})

ROLE_SCOPES = {
    RoleEnum.USER.value: USER_SCOPES,
    RoleEnum.ADMIN.value: ADMIN_SCOPES,
    RoleEnum.SUPER_ADMIN.value: SUPER_ADMIN_SCOPES,
    RoleEnum.EMPLOYEE.value: EMPLOYEE_SCOPES
}
