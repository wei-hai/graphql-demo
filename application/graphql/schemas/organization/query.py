import graphene

from application.graphql.schemas.organization.model import Organization
from application.repos.organization import OrganizationRepository
from application.utils.auth import auth
from application.utils.constant.scope import ScopeEnum


class OrganizationQuery(graphene.ObjectType):
    organization_by_id = graphene.Field(
        Organization,
        id=graphene.Argument(graphene.ID, required=True))

    something = graphene.Field(graphene.String)

    # @auth(scope=ScopeEnum.ORGANIZATION_READ)
    async def resolve_organization_by_id(self, info: graphene.ResolveInfo, id: str):
        repo = OrganizationRepository(info.context["request"].app.db_client)
        org = await repo.add("aha")
        return Organization(id=org["id"], name=org["display_name"])

    @auth(scope=ScopeEnum.ORGANIZATION_WRITE)
    async def resolve_something(self, info: graphene.ResolveInfo):
        return "something"
