from typing import Optional

from pydantic import BaseModel


# Shared properties
class UserBase(BaseModel):
    id: int
    username: Optional[str] = None
    # hashed_password: Optional[str] = None


# Properties to receive on item creation
class UserSignUp(BaseModel):
    username: str
    password: str


class UserUpdate(BaseModel):
    isActive: bool


class UserSignIn(BaseModel):
    username: str
    password: str
