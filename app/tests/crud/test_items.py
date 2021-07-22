from app.tests.factories.item import ItemFactory


def test_item_factory():
    item1 = ItemFactory()
    item2 = ItemFactory()
    assert item1.title == item2.title
