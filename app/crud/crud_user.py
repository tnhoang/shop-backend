from app.schemas.user import UserSignUp
from fastapi.encoders import jsonable_encoder
import sqlalchemy
from app.models.user import User
from app.crud.base import CRUDBase

from app.db.session import Session
from app.core.authen_handler import auth_handler


class CRUDUser(CRUDBase):
    def get_by_username(self, username: str):
        return self.db.query(self.model).filter(self.model.username == username).first()

    def create(self, obj_schema: UserSignUp):
        encoded_data: dict = jsonable_encoder(obj_schema)
        hashed_password = auth_handler.encode_password(encoded_data["password"])
        encoded_data.update({"hashed_password": hashed_password})
        encoded_data.pop("password", None)

        obj = self.model(**encoded_data)
        self.db.add(obj)
        try:
            self.db.commit()
        # Raise IntegrityError when conflict with an existed object.
        except sqlalchemy.exc.IntegrityError as e:
            self.db.rollback()
            return False
        self.db.refresh(obj)
        return obj


user = CRUDUser(User, Session())
