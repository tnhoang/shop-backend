from typing import Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    title: str