from typing import Optional
from pydantic import BaseModel


class ClientIn(BaseModel):
    """Client base model."""

    name: str
    address_line_1: str
    address_line_2: Optional[str]
    city: str


class ClientOut(ClientIn):
    """Client model used to return data."""

    id: int
