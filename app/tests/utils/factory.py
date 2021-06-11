import factory

from app.models.item import Item
from app.models.user import User


class BaseFactory(factory.Factory):
    id = factory.Sequence(lambda n: n)


class UserFactory(BaseFactory):
    class Meta:
        model = User

    full_name = factory.Faker("name")
    email = factory.Faker("email")
    is_active = True
    is_superuser = False


class ItemFactory(BaseFactory):
    class Meta:
        model = Item

    title = "title"
    description = "description"
    # owner = factory.SubFactory(UserFactory)
