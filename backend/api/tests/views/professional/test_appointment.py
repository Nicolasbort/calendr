import json

import pytest
from api.models.appointment import Appointment
from django.urls import reverse


@pytest.mark.django_db
class TestAppointmentViewSet:
    @staticmethod
    def test_create_appointment(professional_api, professional, patient, session):
        data = {
            "patient": str(patient.id),
            "session": str(session.id),
            "date": "2023-04-10",  # Monday
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        appointment = Appointment.objects.first()

        assert appointment is not None
        assert appointment.professional.id == professional.id
        assert appointment.patient.id == patient.id
        assert appointment.session.id == session.id
        assert appointment.date.strftime("%Y-%m-%d") == "2023-04-10"
        assert appointment.duration == 30
        assert appointment.type == "online"

    @staticmethod
    def test_create_appointment_invalid_date(professional_api, patient, session):
        data = {
            "patient": str(patient.id),
            "session": str(session.id),
            "date": "2023-04-11",  # Tuesday
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        response_data = response.json()

        assert response.status_code == 400
        assert "session" in response_data
        assert response_data["session"] == [
            "Ensure the appointment date is in the correct day of the week"
        ]

    @staticmethod
    def test_create_appointment_other_professional(
        professional_api, professional, other_professional, patient, session
    ):
        data = {
            "professional": str(other_professional.id),
            "patient": str(patient.id),
            "session": str(session.id),
            "date": "2023-04-10",  # Monday
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        appointment = Appointment.objects.first()

        assert appointment is not None
        assert appointment.professional.id == professional.id
        assert appointment.patient.id == patient.id
        assert appointment.session.id == session.id
        assert appointment.duration == 30
        assert appointment.type == "online"
