import graphene


class User(graphene.ObjectType):
    id = graphene.Field(graphene.ID, required=True, description="abcd id")
    name = graphene.Field(graphene.String, required=True, description="user name")
    organization_id = graphene.Field(graphene.ID, required=True)
    organization = graphene.Field("application.graphql.schemas.organization.model.Organization", required=True)

    def resolve_organization(self, info):
        from application.graphql.schemas.organization.model import Organization
        return Organization(id=self.organization_id, name="abc")
