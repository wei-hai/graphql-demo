"""
Role
"""
import sqlalchemy as sa

from application.models.base import Base, UUIDMixin, TimestampMixin, SoftDeleteMixin
from application.utils.constant.role import RoleEnum


class Role(Base, UUIDMixin, TimestampMixin, SoftDeleteMixin):
    """
    Role model
    """

    __tablename__ = "role"
    user_id = sa.Column(sa.String(32), nullable=False)
    user_role = sa.Column(sa.String(32), nullable=False, default=RoleEnum.USER.value)
