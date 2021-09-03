from app.schemas.user import UserSignUp
from app.crud.crud_user import CRUDUser
from app.models.user import User
from app.tests.factories.user import UserCreateInDB, UserFactory

from .test_base_crud import TestCreate, TestDelete, TestGet, TestGetMulti, TestUpdate


class TestUserGet(TestGet):
    __test__ = True
    model = User
    schema = UserSignUp
    factory = UserCreateInDB
    crud = CRUDUser


# class TestUserUpdate(TestUpdate):
#     __test__ = True
#     model = User
#     schema = UserSignUp
#     factory = UserCreateInDB
#     crud = CRUDUser
#     NEW_DATA = {"is_active": False}


class TestUserDelete(TestDelete):
    __test__ = True
    model = User
    schema = UserSignUp
    factory = UserCreateInDB
    crud = CRUDUser


class TestUserGetMulti(TestGetMulti):
    __test__ = True
    model = User
    schema = UserSignUp
    factory = UserCreateInDB
    crud = CRUDUser
