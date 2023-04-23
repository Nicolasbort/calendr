import json

import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCustomerViewSet:
    @staticmethod
    def test_me(patient_api, patient):
        url = reverse("api:customer-me")

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_patient = response.json()

        assert str(patient.id) == returned_patient["id"]
        assert patient.profile.first_name == returned_patient["first_name"]
        assert patient.profile.last_name == returned_patient["last_name"]

    @staticmethod
    def test_update_patient(patient_api, patient):
        url = reverse("api:customer-me")

        data = {
            "first_name": "Update First",
            "last_name": "Update Last",
            "email": "update@example.com",
            "phone": "549999999",
        }

        response = patient_api.patch(url, data)

        assert response.status_code == 200

        returned_patient = response.json()

        patient.refresh_from_db()

        assert str(patient.id) == returned_patient["id"]
        assert patient.profile.full_name == returned_patient["full_name"]
        assert patient.profile.first_name == data["first_name"]
        assert patient.profile.last_name == data["last_name"]
        assert patient.email == data["email"]
        assert patient.phone == data["phone"]

        assert patient.first_name != data["first_name"]
        assert patient.last_name != data["last_name"]
