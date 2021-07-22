from app.models.item import Item
from app.crud.base import CRUDBase


class CRUDItem(CRUDBase):
    pass


item = CRUDItem(Item)
