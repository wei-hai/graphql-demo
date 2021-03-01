"""
OrganizationRepository
"""

from typing import Any, Dict

from application.models.organization import Organization
from application.repos.base import BaseRepository


class OrganizationRepository(BaseRepository):
    """
    OrganizationRepository
    """

    async def add(self, name: str) -> Dict[str, Any]:
        """
        Add an organization
        :param organization:
        :return:
        """
        organization = Organization()
        organization.display_name = name
        async with self.db_client.primary_session() as session:
            async with session.begin():
                session.add(organization)
            await session.commit()
            await session.refresh(organization)
            return organization.__dict__
