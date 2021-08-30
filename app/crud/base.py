from typing import Any, Dict, TypeVar, Union

import sqlalchemy
from pydantic import BaseModel
from fastapi.encoders import jsonable_encoder

from app.db.base_class import Base
from app.db.session import Session

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)


class CRUDBase:
    def __init__(self, model: ModelType, session: Session):
        self.model: Base = model
        self.db = session

    def get(self, id: int):
        return self.db.query(self.model).filter(self.model.id == id).first()

    def get_multi(self, skip: int = 0, limit: int = 100):
        return self.db.query(self.model).offset(skip).limit(limit).all()

    def create(self, obj_schema: CreateSchemaType):
        obj_data = jsonable_encoder(obj_schema)
        obj = self.model(**obj_data)

        self.db.add(obj)
        try:
            self.db.commit()
        # Raise IntegrityError when conflict with an existed object.
        except sqlalchemy.exc.IntegrityError as e:
            self.db.rollback()
            return False
        self.db.refresh(obj)
        return obj

    def update(self, obj: ModelType, obj_schema: Union[UpdateSchemaType, Dict[str, Any]]):
        obj_data = jsonable_encoder(obj)

        if isinstance(obj_schema, dict):
            update_data = obj_schema
        else:
            update_data = obj_schema.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(obj, field, update_data[field])

        self.db.add(obj)
        self.db.commit()
        self.db.refresh(obj)
        return obj

    def delete(self, id: int):
        obj = self.db.query(self.model).get(id)
        if not obj:
            return False
        self.db.delete(obj)
        self.db.commit()
        return True
