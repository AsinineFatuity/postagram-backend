from rest_framework import status

from core.fixtures.user import user
from core.fixtures.post import post


class TestUserViewSet:
    endpoint = "/api/user/"

    def test_list(self, client, user):
        response = client.get(f"{self.endpoint}")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1

    def test_retrieve(self, client, user):
        client.force_authenticate(user=user)
        response = client.get(f"{self.endpoint}{user.public_id}/")
        assert response.status_code == status.HTTP_200_OK
        assert response.data["id"] == user.public_id.hex

    def test_create(self, client):
        data = {
            "email": "testme@yopmail.com",
            "username": "test_name",
            "password": "test_pwd",
            "first_name": "Test",
            "last_name": "Me",
        }
        response = client.post(f"{self.endpoint}", data)
        assert response.status_code == status.HTTP_405_METHOD_NOT_ALLOWED

    def test_update(self, user, client):
        data = {"email": "updatedemeil@update.com"}
        client.force_authenticate(user=user)
        response = client.patch(f"{self.endpoint}{str(user.public_id)}/", data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["email"] == data["email"]
