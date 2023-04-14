from api.models.patient import Patient
from api.models.professional import Professional
from api.serializers.address import CreateAddressSerializer
from api.serializers.generic import BaseProfileSerializer, BaseSerializer
from api.serializers.plan import PlanSerializer
from api.serializers.profession import ProfessionSerializer


class ProfessionalSignupSerializer(BaseProfileSerializer, BaseSerializer):
    address = CreateAddressSerializer(required=False)
    plan = PlanSerializer(read_only=True)
    profession = ProfessionSerializer(read_only=True)

    class Meta:
        model = Professional
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at", "profile")
        depth = 1

    def create(self, validated_data) -> Professional:
        address = validated_data.pop("address", None)

        if address is not None:
            serializer = CreateAddressSerializer(data=address)
            serializer.is_valid(raise_exception=True)

            validated_data["address"] = serializer.save()

        return super().create(validated_data, Professional)


class PatientSignupSerializer(BaseProfileSerializer, BaseSerializer):
    class Meta:
        model = Patient
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at", "profile")

    def create(self, validated_data) -> Patient:
        return super().create(validated_data, Patient)
