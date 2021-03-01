"""
AsyncDataLoader
"""
from typing import TypeVar, List

from aiodataloader import DataLoader

T = TypeVar("T")


class AsyncDataLoader(DataLoader):
    """
    AsyncDataLoader
    """
    max_batch_size = 200

    def __init__(self, context):
        """
        Init
        """
        self.context = context
        super().__init__()

    async def batch_load_fn(self, keys) -> List[T]:
        """
        batch_load_fn
        """
        raise NotImplementedError("Must implement batch_load_fn")
