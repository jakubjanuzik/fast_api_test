from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    """Base model with shared properties."""

    email: Optional[EmailStr] = None
    is_active: Optional[bool] = True
    is_superuser: bool = False
    full_name: Optional[str] = None


class UserIn(UserBase):
    """Model used for user creation."""

    email: EmailStr
    password: str


|class UserUpdate(UserBase):
    """Model used for user update."""
    password: Optional[str] = None



class User(UserBase):
    """Generic model."""
    pass


