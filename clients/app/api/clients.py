from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import ClientOut, ClientIn
from app.api import db_manager

clients = APIRouter()


@clients.get("/", response_model=List[ClientOut])
async def get_all_clients():
    """Get all clients."""
    return await db_manager.get_all_clients()


@clients.get("/{id}", response_model=ClientOut)
async def get_client(id: int):
    """Get client by ID handler."""
    client = await db_manager.get_client_by_id(id)
    if not client:
        return HTTPException(status_code=404, detail="Client not found")
    return client


@clients.put("/{id}")
async def update_client(id: int, payload: ClientIn):
    """Update client HTTP Handler."""
    client = await db_manager.get_client_by_id(id)
    if not client:
        return HTTPException(status_code=404, detail="Client not found")

    update_data = payload.dict(exclude_unset=True)

    client_in_db = ClientIn(**client)

    updated_client = client_in_db.copy(update=update_data)

    return await db_manager.update_client(id, updated_client)


@clients.delete("/{id}")
async def delete_client(id):
    """Delete client HTTP handler."""
    return await db_manager.delete_client(id)
