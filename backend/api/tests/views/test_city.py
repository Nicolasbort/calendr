import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCityViewSet:
    @staticmethod
    def test_city_creation(admin_api):
        data = {"name": "Pelotas", "state": "RS"}

        url = reverse("api:city-list")

        response = admin_api.post(url, data)

        assert response.status_code == 201
