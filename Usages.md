Notes:
- factory and crud can not using the same session.
- If bind session to Factory, cannot using that session in query again ([reference](https://stackoverflow.com/questions/22887897/how-to-use-factory-boy-with-sqlalchemy-session-lazy-loaded-correctly))
- migrate: alembic revision --autogenerate -m ""
- upgrade: alembic upgrade head

``` python
    # FAIL: Can not using session like this
    def test_qq(self):
        from app.tests.factories.item import ItemFactory
        factory = ItemFactory
        factory._meta.sqlalchemy_session = self.session # bind session to factory here

        all = self.session.query(Item).all() # can not query this 

    # SUCCESS: create a new session instead
    def test_qq(self):
        # Used factory to create object
        from app.tests.factories.item import ItemFactory
        factory = ItemFactory
        factory._meta.sqlalchemy_session = self.session

        connection = engine.connect()
        trans = connection.begin()
        session = Session(bind=connection)

        all = session.query(Item).all() # It works
```

- Generate json from factory and parse to Pydantic

``` python
    json = factory.stub().__dict__
    item = UserCreate.parse_obj(json)
```