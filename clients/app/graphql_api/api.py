import graphene
from app import db_manager
from app.graphql_api.types import Client


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    client = graphene.Field(Client, id=graphene.Int(required=True))
    all_clients = graphene.List(of_type=Client)

    async def resolve_hello(self, info, name):
        """Test resolver."""
        return "Hello " + name

    async def resolve_all_clients(self, info):
        """Resolve all clients."""
        clients = await db_manager.get_all_clients()

        return [
            Client(
                id=client["id"],
                name=client["name"],
                city=client["city"],
                address_line_1=client["address_line_1"],
                address_line_2=client["address_line_2"],
            )
            for client in clients
        ]

    async def resolve_client(self, info, id):
        """Resolve client by id."""
        val = await db_manager.get_client_by_id(id)

        return Client(
            id=val["id"],
            name=val["name"],
            city=val["city"],
            address_line_1=val["address_line_1"],
            address_line_2=val["address_line_2"],
        )
