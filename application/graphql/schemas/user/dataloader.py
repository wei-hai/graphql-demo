from typing import List

from application.graphql.schemas.user.model import User
from application.graphql.utils.dataloader import AsyncDataLoader


class UserDataLoader(AsyncDataLoader):

    async def batch_load_fn(self, keys) -> List[User]:
        print("keys")
        print(keys)
        response = []
        for key in keys:
            response.append(User(id=key, name="name+" + key, organization_id=key))
        return response
