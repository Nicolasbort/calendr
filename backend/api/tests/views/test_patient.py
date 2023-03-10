import json

import pytest
from api.models import Patient, Profile
from django.urls import reverse


@pytest.mark.django_db
class TestPatientViewSet:
    @staticmethod
    def test_list_patient(admin_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        expected_fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "username",
            "phone",
            "profile",
            "professional",
            "notify_pending_payment",
            "created_at",
            "modified_at",
        ]

        response = admin_api.get(url)

        assert response.status_code == 200
        assert set(response.json().keys()) == set(expected_fields)

    @staticmethod
    def test_create_patient(admin_api, professional):
        url = reverse("api:patient-list")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "patient@example.com",
            "username": "patient",
            "phone": "99999999",
            "notify_pending_payment": True,
            "professional": str(professional.id),
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        patient = Patient.objects.first()

        assert patient is not None

        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None

        assert profile.first_name == "First"
        assert profile.last_name == "Last"
        assert profile.email == "patient@example.com"
        assert profile.username == "patient"
        assert profile.phone == "99999999"

        assert patient.professional.id == professional.id
        assert patient.notify_pending_payment is True

    @staticmethod
    def test_create_patient_no_phone(admin_api, professional):
        url = reverse("api:patient-list")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "patient@example.com",
            "username": "patient",
            "notify_pending_payment": True,
            "professional": str(professional.id),
        }

        response = admin_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        patient = Patient.objects.first()

        assert patient is not None

        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None

        assert profile.first_name == "First"
        assert profile.last_name == "Last"
        assert profile.email == "patient@example.com"
        assert profile.username == "patient"
        assert profile.phone == None

        assert patient.professional.id == professional.id
        assert patient.notify_pending_payment is True

    @staticmethod
    def test_update_patient(admin_api, patient, other_professional):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        data = {
            "first_name": "Update First",
            "last_name": "Update Last",
            "email": "update-patient@example.com",
            "username": "update-patient",
            "phone": "8888888",
            "notify_pending_payment": False,
            "professional": str(other_professional.id),
        }

        response = admin_api.patch(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        patient.refresh_from_db()
        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None
        assert profile.first_name == "Update First"
        assert profile.last_name == "Update Last"
        assert profile.email == "update-patient@example.com"
        assert profile.username == "update-patient"
        assert profile.phone == "8888888"

        assert patient.professional.id == other_professional.id
        assert patient.notify_pending_payment is False

    @staticmethod
    def test_update_patient_invalid_email(admin_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        data = {
            "email": "invalid_email",
        }

        response = admin_api.patch(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        patient.refresh_from_db()
        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None
        assert profile.email != "invalid_email"
