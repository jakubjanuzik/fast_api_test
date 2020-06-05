from sqlalchemy import (Boolean, Column, Integer, MetaData, String, Table,
                        create_engine)

from app.config import settings
from databases import Database

DATABASE_URL = (
    f"postgresql://{settings.database_user}:{settings.database_name}"
    f"@{settings.database_host}:{settings.database_port}/{settings.database_name}"
)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("first_name", String(64)),
    Column("last_name", String(64)),
    Column("email", String(64), unique=True, index=True, nullable=False),
    Column("hashed_password", String(128), nullable=False),
    Column("is_active", Boolean, default=True),
    Column("is_superuser", Boolean, default=False),
)


database = Database(DATABASE_URL)
