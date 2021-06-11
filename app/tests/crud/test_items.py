from app.tests.utils.factory import ItemFactory


def test_item_factory() -> None:
    item = ItemFactory.stub()
    assert item.title == "title"
    assert item.description == "description"
