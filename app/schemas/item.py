from typing import List, Optional

from pydantic import BaseModel


# Shared properties
class ItemBase(BaseModel):
    id: int
    title: Optional[str] = None
    description: Optional[str] = None


# Properties to receive on item creation
class ItemCreate(ItemBase):
    pass
