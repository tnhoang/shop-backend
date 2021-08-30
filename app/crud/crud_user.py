from app.models.user import User
from app.crud.base import CRUDBase

from app.db.session import Session


class CRUDUser(CRUDBase):
    pass


user = CRUDUser(User, Session())
