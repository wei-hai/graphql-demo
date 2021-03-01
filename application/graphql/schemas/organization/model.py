import graphene

from application.graphql.schemas.user.dataloader import UserDataLoader
from application.graphql.schemas.user.model import User


class Organization(graphene.ObjectType):
    user_ids = [str(i) for i in range(210)]
    id = graphene.Field(graphene.ID, required=True)
    name = graphene.Field(graphene.String, required=True)
    users = graphene.Field(graphene.List(User))

    async def resolve_users(self, info):
        data_loader = UserDataLoader(info.context)
        return data_loader.load_many(self.user_ids)
