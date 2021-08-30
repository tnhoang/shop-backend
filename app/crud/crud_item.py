from app.models.item import Item
from app.crud.base import CRUDBase

from app.db.session import Session


class CRUDItem(CRUDBase):
    pass


item = CRUDItem(Item, Session())
