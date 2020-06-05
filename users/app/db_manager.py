from app.api.models import UserIn
from app.db import database, users


async def get_all_users():
    """Call Database and return all users."""
    query = users.select()
    return await database.fetch_all(query=query)


async def get_user_by_id(id: int):
    """Return user by ID."""
    query = users.select(users.c.id == id)
    return await database.fetch_one(query=query)


async def create_user(user: UserIn):
    """Create user object in database."""
