from sqlalchemy import Column, Integer, MetaData, String, Table, create_engine

from app.config import settings
from databases import Database

DATABASE_URL = (
    f"postgresql://{settings.database_user}:{settings.database_name}"
    f"@{settings.database_host}:{settings.database_port}/{settings.database_name}"
)

engine = create_engine(DATABASE_URL)
metadata = MetaData()

clients = Table(
    "clients",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(64)),
    Column("address_line_1", String(64)),
    Column("address_line_2", String(64), nullable=True),
    Column("city", String(64)),
)

database = Database(DATABASE_URL)
