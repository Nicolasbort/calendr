import json

import pytest
from api.models.appointment import Appointment
from django.urls import reverse


@pytest.mark.django_db
class TestAppointmentViewSet:
    @staticmethod
    def test_create_appointment(professional_api, professional, patient, slot):
        data = {
            "patient": str(patient.id),
            "slot": str(slot.id),
            "time_end": "17:00:00",
            "time_start": "16:30:00",
            "price": "150.00",
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        appointment = Appointment.objects.first()

        assert appointment is not None
        assert str(appointment.professional.id) == str(professional.id)
        assert str(appointment.patient.id) == str(patient.id)
        assert str(appointment.slot.id) == str(slot.id)
        assert appointment.time_end.strftime("%H:%M:%S") == "17:00:00"
        assert appointment.time_start.strftime("%H:%M:%S") == "16:30:00"
        assert appointment.duration == 30
        assert str(appointment.price) == "150.00"
        assert appointment.type == "online"

    @staticmethod
    def test_create_appointment_invalid_time_range(
        professional_api, professional, patient, slot
    ):
        data = {
            "patient": str(patient.id),
            "slot": str(slot.id),
            "time_end": "17:01:00",
            "time_start": "16:31:00",
            "price": "150.00",
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        response_data = response.json()

        assert response.status_code == 400
        assert "non_field_errors" in response_data
        assert response_data["non_field_errors"] == [
            "Ensure the appointment is between the slot time start and end"
        ]

    @staticmethod
    def test_create_appointment_invalid_duration(
        professional_api, professional, patient, slot
    ):
        data = {
            "patient": str(patient.id),
            "slot": str(slot.id),
            "time_end": "17:00:00",
            "time_start": "16:31:00",
            "price": "150.00",
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        response_data = response.json()

        assert response.status_code == 400
        assert "non_field_errors" in response_data
        assert response_data["non_field_errors"] == [
            f"Ensure the duration of the appointment is mulitple of {slot.calendar.duration}"
        ]

    @staticmethod
    def test_create_appointment_other_professional(
        professional_api, professional, other_professional, patient, slot
    ):
        data = {
            "professional": str(other_professional.id),
            "patient": str(patient.id),
            "slot": str(slot.id),
            "time_end": "17:00:00",
            "time_start": "16:30:00",
            "price": "150.00",
            "type": "online",
        }

        url = reverse("api:appointment-list")

        response = professional_api.post(
            url, json.dumps(data), content_type="application/json"
        )

        assert response.status_code == 201

        appointment = Appointment.objects.first()

        assert appointment is not None
        assert str(appointment.professional.id) == str(professional.id)
        assert str(appointment.patient.id) == str(patient.id)
        assert str(appointment.slot.id) == str(slot.id)
        assert appointment.time_end.strftime("%H:%M:%S") == "17:00:00"
        assert appointment.time_start.strftime("%H:%M:%S") == "16:30:00"
        assert appointment.duration == 30
        assert str(appointment.price) == "150.00"
        assert appointment.type == "online"
