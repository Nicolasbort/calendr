from datetime import datetime

from api.constants.session import WeekDayChoices
from api.models.appointment import Appointment
from api.serializers.customer.session import CustomerSessionSerializer
from api.serializers.generic import BaseSerializer, ReadOnlySerializer
from api.tasks.google_calendar import schedule_event
from rest_framework.serializers import ValidationError


class CustomerAppointmentSerializer(ReadOnlySerializer):
    session = CustomerSessionSerializer()

    class Meta:
        model = Appointment
        exclude = (
            "deleted_at",
            "patient",
        )


class CustomerCreateAppointmentSerializer(BaseSerializer):
    class Meta:
        model = Appointment
        read_only_fields = (
            "id",
            "link",
            "created_at",
            "modified_at",
        )
        exclude = (
            "deleted_at",
            "patient",
        )

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
