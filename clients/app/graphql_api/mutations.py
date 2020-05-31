import graphene
from app import db_manager
from app.api.models import ClientIn
from app.graphql_api.types import Client


class CreateClient(graphene.Mutation):
    """Mutation class used to create client object in database."""

    ok = graphene.Boolean()
    client = graphene.Field(lambda: Client)

    class Arguments:
        name = graphene.String()
        address_line_1 = graphene.String()
        address_line_2 = graphene.String(required=False)
        city = graphene.String()

    async def mutate(root, info, name, address_line_1, city, address_line_2=None):
        """Call Database and create a client."""
        client_data = ClientIn(
            name=name,
            address_line_1=address_line_1,
            address_line_2=address_line_2,
            city=city,
        )
        client_id = await db_manager.create_client(client=client_data)
        client = Client(**client_data.dict(), id=client_id)

        return CreateClient(client=client, ok=True)


class DeleteClient(graphene.Mutation):
    """Mutation class used to delete client object in database."""

    ok = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    async def mutate(root, info, id):
        """Call Database and remove a client."""

        await db_manager.delete_client(id)

        return DeleteClient(ok=True)


class Mutations(graphene.ObjectType):
    create_client = CreateClient.Field()
    delete_client = DeleteClient.Field()
