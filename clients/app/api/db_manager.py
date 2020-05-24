from app.api.db import clients, database
from app.api.models import ClientIn


async def get_all_clients():
    """Call DB and return all clients."""
    query = clients.select()
    return await database.fetch_all(query=query)


async def get_client_by_id(id: int):
    """Return client by ID."""
    query = clients.select(clients.c.id == id)
    return await database.fetch_one(query=query)


async def update_client(id: int, payload: ClientIn):
    """Update Client object in database."""
    query = clients.update().where(clients.c.id == id).values(**payload.dict())
    return await database.execute(query=query)


async def delete_client(id: int):
    """Delete client in Database."""
    query = clients.delete().where(clients.c.id == id)
    return await database.execute(query=query)
