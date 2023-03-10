from api.models.patient import Patient
from api.serializers.base_profile import BaseProfileSerializer


class PatientSerializer(BaseProfileSerializer):
    class Meta:
        model = Patient
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
            "profile",
        )
        exclude = ("deleted_at",)

    def create(self, validated_data) -> Patient:
        return super().create(validated_data, Patient)
