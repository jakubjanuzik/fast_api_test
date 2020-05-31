import graphene


class Client(graphene.ObjectType):
    """Graphene client object type."""

    id = graphene.Int()
    name = graphene.String()
    address_line_1 = graphene.String()
    address_line_2 = graphene.String()
    full_address = graphene.String()
    city = graphene.String()

    def resolve_full_address(parent, info):
        """Combine address_line_1, address_line_2 and city."""
        if parent.address_line_2:
            return (
                f"{parent.address_line_1} \n {parent.address_line_2} \n {parent.city}"
            )
        return f"{parent.address_line_1} \n {parent.city}"
