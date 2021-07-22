from app.models.item import Item
from app.tests.conftest import session
from app.tests.factories.base_factory import BaseFactory


class ItemFactory(BaseFactory):
    class Meta:
        model = Item
        sqlalchemy_session = session

    title = "title"
    description = "description"
