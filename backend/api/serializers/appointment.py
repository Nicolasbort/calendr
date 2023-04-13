from datetime import datetime

from api.constants.session import WeekDayChoices
from api.models.appointment import Appointment
from api.serializers.generic import BaseSerializer, ReadOnlySerializer
from api.serializers.session import AppointmentSessionSerializer
from api.tasks.google_calendar import schedule_event
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class AppointmentSerializer(ReadOnlySerializer):
    duration = serializers.ReadOnlyField()
    session = AppointmentSessionSerializer(read_only=True)

    class Meta:
        model = Appointment
        exclude = ("deleted_at",)


class CreateAppointmentSerializer(BaseSerializer):
    duration = serializers.ReadOnlyField()

    class Meta:
        model = Appointment
        read_only_fields = (
            "id",
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
