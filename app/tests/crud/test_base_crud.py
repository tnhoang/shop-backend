from typing import Dict

from app.crud.base import CRUDBase
from app.tests.common import Session, engine
from fastapi.encoders import jsonable_encoder


class Setup:
    __test__ = False  # This will prevent run test cases in abstract class

    model = None
    schema = None
    factory = None
    crud = None

    def setup_method(self):
        """setup any state tied to the execution of the given method in a
        class.  setup_method is invoked for every test method of a class.
        """
        # connect to the database
        self.connection = engine.connect()
        # begin a non-ORM transaction
        self.trans = self.connection.begin()
        # bind an individual Session to the connection
        self.session = Session(bind=self.connection)

        # Prepare
        self.crud: CRUDBase = self.crud(self.model, self.session)
        self.generator = DBInstanceGenerator(factory=self.factory, crud=self.crud, schema=self.schema)

    def teardown_method(self):
        self.session.close()

        # rollback - everything that happened with the
        # Session above (including calls to commit())
        # is rolled back.
        self.trans.rollback()

        # return connection to the Engine
        self.connection.close()


class TestGet(Setup):
    def test_when_item_existed_then_return_item(self):
        expected_item = self.generator.create_objects(1)
        actual_item = self.crud.get(expected_item.id)
        assert actual_item == expected_item

    def test_when_item_does_not_exist_then_return_None(self):
        assert self.crud.get(1) == None


class TestGetMulti(Setup):
    def test_get_multi_objects_successfully(self):
        expected_objects = self.generator.create_objects(2)
        actual_objects = self.crud.get_multi()

        sort_by_id = lambda obj: obj.id
        assert sorted(actual_objects, key=sort_by_id) == sorted(expected_objects, key=sort_by_id)


class TestCreate(Setup):
    def test_when_data_is_valid_then_return_obj_sucessfully(self):
        raw_data: Dict = self.factory.stub().__dict__
        parsed_data = self.schema.parse_obj(raw_data)

        expected_item = self.crud.create(parsed_data)
        assert parsed_data.id == expected_item.id

    # TODO: test when data is invalid


class TestUpdate(Setup):
    def test_when_new_data_is_valid_then_return_updated_obj(self):
        existed_obj = self.generator.create_objects(1)
        raw_data: Dict = self.factory.stub().__dict__
        parsed_data = self.schema.parse_obj(raw_data)

        updated_obj = self.crud.update(existed_obj, parsed_data)
        updated_json: Dict = jsonable_encoder(updated_obj)

        for field in raw_data.keys():
            assert raw_data[field] == updated_json[field]

    # TODO: test when data is invalid


class TestDelete(Setup):
    def test_when_object_in_db_then_delete_it_and_return_true(self):
        expected_item = self.generator.create_objects(1)
        assert self.crud.delete(expected_item.id) == True

    def test_when_object_not_in_db_then_return_false(self):
        assert self.crud.delete(1) == False


class DBInstanceGenerator:
    def __init__(self, factory, schema, crud):
        self.factory = factory
        self.schema = schema
        self.crud = crud

    def create_objects(self, quantity=2):
        if not quantity or quantity == 1:
            return self._create()
        return [self._create() for _ in range(quantity)]

    def _create(self):
        raw_data: Dict = self.factory.stub().__dict__
        parsed_data = self.schema.parse_obj(raw_data)
        created_obj = self.crud.create(parsed_data)
        return created_obj
