import pytest
from core.user.models import User

data_user = {
    "username": "test_user",
    "email": "test@yopmail.com",
    "first_name": "Test",
    "last_name": "User",
    "password": "12345",
}

data_superuser = {
    "username": "test_superuser",
    "email": "testsuperuser@yopmail.com",
    "first_name": "Test",
    "last_name": "Superuser",
    "password": "test_pwd",
}


@pytest.mark.django_db
def test_create_user():
    user = User.objects.create_user(**data_user)
    assert user.username == data_user["username"]
    assert user.email == data_user["email"]
    assert user.first_name == data_user["first_name"]
    assert user.last_name == data_user["last_name"]


@pytest.mark.django_db
def test_create_superuser():
    super_user = User.objects.create_superuser(**data_superuser)
    assert super_user.username == data_superuser["username"]
    assert super_user.email == data_superuser["email"]
    assert super_user.first_name == data_superuser["first_name"]
    assert super_user.last_name == data_superuser["last_name"]
    assert super_user.is_superuser == True
    assert super_user.is_staff == True
