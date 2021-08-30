from app.crud.crud_item import CRUDItem
from app.models.item import Item
from app.schemas.item import ItemCreate
from app.tests.factories.item import ItemFactory

from .test_base_crud import TestCreate, TestDelete, TestGet, TestGetMulti, TestUpdate


class TestItemGet(TestGet):
    __test__ = True
    model = Item
    schema = ItemCreate
    factory = ItemFactory
    crud = CRUDItem


class TestItemCreate(TestCreate):
    __test__ = True
    model = Item
    schema = ItemCreate
    factory = ItemFactory
    crud = CRUDItem


class TestItemUpdate(TestUpdate):
    __test__ = True
    model = Item
    schema = ItemCreate
    factory = ItemFactory
    crud = CRUDItem


class TestItemDelete(TestDelete):
    __test__ = True
    model = Item
    schema = ItemCreate
    factory = ItemFactory
    crud = CRUDItem


class TestItemGetMulti(TestGetMulti):
    __test__ = True
    model = Item
    schema = ItemCreate
    factory = ItemFactory
    crud = CRUDItem
