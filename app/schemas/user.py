from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    id: int
    full_name: Optional[str] = None
    email: Optional[str] = None
    hashed_password: Optional[str] = None


# Properties to receive on item creation
class UserCreate(UserBase):
    pass
