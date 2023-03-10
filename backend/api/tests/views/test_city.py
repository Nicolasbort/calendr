import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCityViewSet:
    @staticmethod
    def test_city_list(patient_api, city):
        url = reverse("api:city-detail", kwargs={"pk": city.id})

        response = patient_api.get(url)

        assert response.status_code == 200
        assert set(response.json().keys()) == set(
            [
                "id",
                "name",
                "state",
            ]
        )
