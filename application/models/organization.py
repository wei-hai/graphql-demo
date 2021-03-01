"""
Organization
"""
import sqlalchemy as sa

from application.models.base import Base, SoftDeleteMixin, TimestampMixin, UUIDMixin


class Organization(Base, TimestampMixin, UUIDMixin, SoftDeleteMixin):
    """
    Organization model
    """

    __tablename__ = "organization"
    display_name = sa.Column(sa.String(32), nullable=False)
