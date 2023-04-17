from api.models.appointment import Appointment
from api.models.patient import Patient
from api.models.session import Session
from api.serializers.generic import BaseProfileSerializer, ReadOnlySerializer


class SessionAppointmentSerializer(ReadOnlySerializer):
    class Meta:
        model = Session
        exclude = ("deleted_at",)


class PatientAppointmentSerializer(BaseProfileSerializer, ReadOnlySerializer):
    class Meta:
        model = Patient
        exclude = (
            "deleted_at",
            "profile",
        )


class AppointmentSessionSerializer(ReadOnlySerializer):
    patient = PatientAppointmentSerializer()

    class Meta:
        model = Appointment
        exclude = (
            "deleted_at",
            "session",
        )
