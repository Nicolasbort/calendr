from api.models.patient import Patient
from api.serializers.appointment import AppointmentSerializer
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseSerializer,
    WriteBaseProfileSerializer,
)


class PatientSerializer(WriteBaseProfileSerializer, BaseSerializer):
    appointments = AppointmentSerializer(many=True, read_only=True)

    READ_PROFILE_KEYS = ["phone", "email"]

    class Meta:
        model = Patient
        read_only_fields = (
            "professional",
            "is_confirmed",
            "appointments",
        ) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "deleted_at",
            "profile",
        )

    def get_password(self, validated_data: dict) -> str:
        return validated_data.pop("password", None)

    def create(self, validated_data: dict) -> Patient:
        request = self.context.get("request")
        profile = self.create_profile(validated_data)

        return Patient.objects.create(
            profile=profile,
            professional=request.user.professional,
            **validated_data,
        )
