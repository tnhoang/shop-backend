from app.crud.crud_user import CRUDUser
from app.models.user import User
from app.schemas.user import UserCreate
from app.tests.factories.user import UserFactory

from .test_base_crud import TestCreate, TestDelete, TestGet, TestGetMulti, TestUpdate


class TestUserGet(TestGet):
    __test__ = True
    model = User
    schema = UserCreate
    factory = UserFactory
    crud = CRUDUser


class TestUserCreate(TestCreate):
    __test__ = True
    model = User
    schema = UserCreate
    factory = UserFactory
    crud = CRUDUser


class TestUserUpdate(TestUpdate):
    __test__ = True
    model = User
    schema = UserCreate
    factory = UserFactory
    crud = CRUDUser


class TestUserDelete(TestDelete):
    __test__ = True
    model = User
    schema = UserCreate
    factory = UserFactory
    crud = CRUDUser


class TestUserGetMulti(TestGetMulti):
    __test__ = True
    model = User
    schema = UserCreate
    factory = UserFactory
    crud = CRUDUser
