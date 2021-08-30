from app.models import Item
from app.tests.factories.base_factory import BaseFactory


class ItemFactory(BaseFactory):
    class Meta:
        model = Item

    title = "title"
    description = "description"
