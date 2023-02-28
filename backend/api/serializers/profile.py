from api.models.profile import Profile
from api.serializers.address import AddressSerializer
from api.serializers.plan import PlanSerializer
from api.serializers.profession import ProfessionSerializer
from api.utils.serializers import get_serialized_data
from rest_framework import serializers


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ("uuid, created_at, modified_at",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data: dict):
        profile = Profile(**validated_data)
        profile.set_password(validated_data.get("password"))
        profile.save()

        return profile

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["profession"] = get_serialized_data(
            ProfessionSerializer, instance.profession
        )
        data["plan"] = get_serialized_data(PlanSerializer, instance.plan)
        data["address"] = get_serialized_data(AddressSerializer, instance.address)

        return data
