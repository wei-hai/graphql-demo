"""
User
"""
import sqlalchemy as sa

from application.models.base import Base, SoftDeleteMixin, TimestampMixin, UUIDMixin


class User(Base, TimestampMixin, UUIDMixin, SoftDeleteMixin):
    """
    User model
    """

    __tablename__ = "user"
    display_name = sa.Column(sa.String(32), nullable=False)
    first_name = sa.Column(sa.String(32), nullable=False)
    last_name = sa.Column(sa.String(32), nullable=False)
    avatar = sa.Column(sa.Text, nullable=True)
