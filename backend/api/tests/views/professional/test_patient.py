import json

import pytest
from api.models import Patient, Profile
from django.urls import reverse


@pytest.mark.django_db
class TestPatientViewSet:
    @staticmethod
    def test_get_patient(professional_api, patient, patient_fields):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        response = professional_api.get(url)

        assert response.status_code == 200
        assert set(response.json().keys()) == set(patient_fields)

    @staticmethod
    def test_get_patient_has_appointments(professional_api, patient, appointment):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        response = professional_api.get(url)

        assert response.status_code == 200

        data = response.json()

        assert str(patient.id) == data["id"]

        for appointment_json in data["appointments"]:
            assert str(appointment.id) == appointment_json["id"]

    @staticmethod
    @pytest.mark.parametrize(
        "first_name, last_name, expected",
        [
            ("Patient", "Lastname", True),
            ("Patient", None, True),
            ("Wrong", None, False),
            ("Patinet", "Lastmnae", True),
            ("Wrong", "Test", False),
            ("Random", "Test", False),
        ],
    )
    def test_list_patient_filter_by_name(
        professional_api, patient, first_name, last_name, expected
    ):
        search_name = first_name
        search_name += f" {last_name}" if last_name else ""

        url = reverse("api:patient-list") + f"?name={search_name}"

        response = professional_api.get(url)

        assert response.status_code == 200

        data = response.json()

        results = data["results"]
        count = data["count"]

        if expected:
            assert count == 1
            assert str(patient.id) == results[0]["id"]
        else:
            assert count == 0

    @staticmethod
    def test_create_patient(professional_api, professional):
        url = reverse("api:patient-list")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "patient@example.com",
            "phone": "99999999",
            "notify_pending_payment": True,
            "notify_appointment": True,
        }

        response = professional_api.post(
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
        assert profile.username == "firstlast"
        assert profile.phone == "99999999"

        assert patient.professional.id == professional.id
        assert patient.notify_pending_payment is True
        assert patient.notify_appointment is True

    @staticmethod
    def test_create_patient_no_phone(professional_api):
        url = reverse("api:patient-list")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "patient@example.com",
            "notify_pending_payment": True,
        }

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

    @staticmethod
    def test_create_patient_other_professional(
        professional_api, professional, other_professional
    ):
        url = reverse("api:patient-list")

        data = {
            "first_name": "First",
            "last_name": "Last",
            "email": "patient@example.com",
            "phone": "5399999999",
            "notify_pending_payment": True,
            "professional": str(other_professional.id),
        }

        response = professional_api.post(
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
        assert profile.username == "firstlast"
        assert profile.phone == "5399999999"

        assert patient.professional.id == professional.id
        assert patient.notify_pending_payment is True

    @staticmethod
    def test_update_patient(
        professional_api, patient, professional, other_professional
    ):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        data = {
            "first_name": "Update First",
            "last_name": "Update Last",
            "email": "update-patient@example.com",
            "phone": "8888888",
            "notify_pending_payment": False,
            "professional": str(other_professional.id),
        }

        response = professional_api.patch(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 200

        patient.refresh_from_db()
        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None
        assert profile.first_name == "Update First"
        assert profile.last_name == "Update Last"
        assert profile.email == "update-patient@example.com"
        assert profile.username == "patientlastname"
        assert profile.phone == "8888888"

        assert patient.professional.id == professional.id
        assert patient.notify_pending_payment is False

    @staticmethod
    def test_update_patient_invalid_email(professional_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        data = {
            "email": "invalid_email",
        }

        response = professional_api.patch(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 400

        patient.refresh_from_db()
        profile = Profile.objects.filter(patient=patient).first()

        assert profile is not None
        assert profile.email != "invalid_email"

    @staticmethod
    def test_list_patient_forbiden(patient_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        response = patient_api.get(url)

        assert response.status_code == 403

    @staticmethod
    def test_create_patient_forbiden(patient_api):
        url = reverse("api:patient-list")

        response = patient_api.post(url, content_type="application/json")

        assert response.status_code == 403

    @staticmethod
    def test_update_patient_forbiden(patient_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        response = patient_api.patch(url, content_type="application/json")

        assert response.status_code == 403

    @staticmethod
    def test_delete_patient_forbiden(patient_api, patient):
        url = reverse("api:patient-detail", kwargs={"pk": patient.id})

        response = patient_api.delete(url)

        assert response.status_code == 403
