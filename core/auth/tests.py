import pytest
from rest_framework import status
from core.fixtures.user import user


class TestAuthenticationViewSet:
    endpoint = "/api/auth/"

    def test_login(self, client, user):
        data = {"email": user.email, "password": "test_pwd"}
        response = client.post(f"{self.endpoint}login/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
        assert response.data["user"]["id"] == user.public_id.hex
        assert response.data["user"]["username"] == user.username
        assert response.data["user"]["email"] == user.email

    @pytest.mark.django_db
    def test_register(self, client):
        data = {
            "username": "loveydovey",
            "email": "loveydovey@yopmail.com",
            "password": "test_pwd",
            "first_name": "Maudlin",
            "last_name": "Allove",
        }
        response = client.post(f"{self.endpoint}register/", data)
        assert response.status_code == status.HTTP_201_CREATED

    def test_refresh(self, client, user):
        data = {"email": user.username, "password": "test_pwd"}
        response = client.post(f"{self.endpoint}login/", data)
        assert response.status_code == status.HTTP_200_OK

        data_refresh = {"refresh": response.data["refresh"]}

        response = client.post(f"{self.endpoint}refresh/", data_refresh)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["access"]
