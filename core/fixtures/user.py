import pytest
from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@yopmail.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "test_pwd",
}


@pytest.fixture
def user(db) -> User:
    return User.objects.create_user(**data_user)
