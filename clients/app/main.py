import graphene as graphene
import uvicorn
from app.api.clients import clients
from app.db import database, engine, metadata
from app.graphql_api.api import Query
from app.graphql_api.mutations import Mutations
from fastapi import FastAPI
from graphql.execution.executors.asyncio import AsyncioExecutor
from starlette.graphql import GraphQLApp

app = FastAPI()
app.add_route(
    "/graphql/",
    GraphQLApp(
        schema=graphene.Schema(query=Query, mutation=Mutations),
        executor_class=AsyncioExecutor,
    ),
)

metadata.create_all(engine)

app.include_router(clients, prefix="/api/v1/clients", tags=["clients"])


@app.on_event("startup")
async def startup():
    """Connect to database on startup."""
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    """Disconnect database while closing app."""
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
