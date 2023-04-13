from api.models.patient import Patient
from api.serializers.appointment import AppointmentSerializer
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseProfileSerializer,
    BaseSerializer,
)


class PatientSerializer(BaseProfileSerializer, BaseSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    class Meta:
        model = Patient
        read_only_fields = (
            "professional",
            "appointments",
        ) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "deleted_at",
            "profile",
        )

    def create(self, validated_data) -> Patient:
        return super().create(validated_data, Patient)

    def save(self, **kwargs):
        request = self.context.get("request")

        return super().save(professional=request.user.professional)
