from fastapi import FastAPI
from app.api.db import metadata, database, engine
from app.api.clients import clients

app = FastAPI()

metadata.create_all(engine)

app.include_router(clients, prefix="/api/v1/clients", tags=["clients"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
def read_root():
    return {"Hello": "World"}
