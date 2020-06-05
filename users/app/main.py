import uvicorn
from app.db import database
from fastapi import FastAPI

app = FastAPI()


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
    return {"Hello": "Clients"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
