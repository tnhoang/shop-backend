import factory
from app.models.user import User
from app.tests.conftest import session
from app.tests.factories.base_factory import BaseFactory


class UserFactory(BaseFactory):
    class Meta:
        model = User

    full_name = factory.Faker("name")
    email = factory.Faker("email")
    is_active = True
    is_superuser = False
