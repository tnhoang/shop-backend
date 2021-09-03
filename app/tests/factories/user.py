import factory
from app.models.user import User
from app.tests.factories.base_factory import BaseFactory


class UserFactory(BaseFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    hashed_password = factory.Faker("text")
    is_active = True
    is_superuser = False


class UserCreateInDB(BaseFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    password = factory.Faker("name")
