from datetime import datetime

from api.constants.session import WeekDayChoices
from api.models.appointment import Appointment
from api.serializers.generic import BaseSerializer
from api.tasks.google_calendar import schedule_event
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class AppointmentSerializer(BaseSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        read_only_fields = (
            "id",
            "professional",
            "duration",
            "link",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)

    def validate_session(self, session):
        date = self.initial_data.get("date")
        date = datetime.strptime(date, "%Y-%m-%d")

        if date.weekday() != WeekDayChoices.to_python(session.week_day):
            raise ValidationError(
                f"Ensure the appointment date is in the correct day of the week"
            )

        return session

    def create(self, validated_data):
        appointment = super().create(validated_data)

        schedule_event.delay(
            professional_id=appointment.professional.id,
            appointment_id=appointment.id,
            patient_ids=[appointment.patient.id],
        )

        return appointment

    def save(self, **kwargs):
        request = self.context.get("request")

        return super().save(professional=request.user.professional)


class CustomerAppointmentSerializer(BaseSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        read_only_fields = (
            "id",
            "duration",
            "patient",
            "link",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)

    def validate_session(self, session):
        date = self.initial_data.get("date")
        date = datetime.strptime(date, "%Y-%m-%d")

        if date.weekday() != WeekDayChoices.to_python(session.week_day):
            raise ValidationError(
                f"Ensure the appointment date is in the correct day of the week"
            )

        return session

    def create(self, validated_data):
        appointment = super().create(validated_data)

        schedule_event.delay(
            professional_id=appointment.professional.id,
            appointment_id=appointment.id,
            patient_ids=[appointment.patient.id],
        )

        return appointment

    def save(self, **kwargs):
        request = self.context.get("request")

        return super().save(patient=request.user.patient)
