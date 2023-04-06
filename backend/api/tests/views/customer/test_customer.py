import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCustomerViewSet:
    @staticmethod
    def test_me(patient_api, patient):

        url = reverse("api:logged_user")

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_profile = response.json()

        profile = patient.profile

        assert str(profile.id) == returned_profile["id"]
        assert profile.full_name == returned_profile["full_name"]
