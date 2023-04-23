from api.models.patient import Patient
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.professional import Professional
from api.serializers.address import CreateAddressSerializer
from api.serializers.generic import BaseSerializer, WriteBaseProfileSerializer
from api.serializers.plan import PlanSerializer
from api.serializers.profession import ProfessionSerializer
from rest_framework import serializers


class ProfessionalSignupSerializer(WriteBaseProfileSerializer, BaseSerializer):
    full_name = serializers.ReadOnlyField()
    address = CreateAddressSerializer(required=False)
    plan = PlanSerializer(read_only=True)
    profession = ProfessionSerializer(read_only=True)

    class Meta:
        model = Professional
        read_only_fields = (
            "id",
            "username",
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

        plan = Plan.get_default_plan()
        profession = Profession.get_default_profession()
        profile = self.create_profile(validated_data)

        return Professional.objects.create(
            profile=profile,
            plan=plan,
            profession=profession,
            **validated_data,
        )


class PatientSignupSerializer(WriteBaseProfileSerializer, BaseSerializer):
    class Meta:
        model = Patient
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = (
            "deleted_at",
            "profile",
            "is_confirmed",
        )

    def create(self, validated_data) -> Patient:
        profile = self.create_profile(validated_data)

        return Patient.objects.create(
            profile=profile,
            **validated_data,
        )
