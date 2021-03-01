"""
Base Repository
"""

from application.services.common.db_client import AsyncDatabaseClient


class BaseDBRepository:
    """
    BaseRepository
    """

    def __init__(self, db_client: AsyncDatabaseClient):
        """
        Init
        @param db_client:
        """
        self.db_client = db_client
