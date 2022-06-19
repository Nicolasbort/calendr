from rest_framework import serializers

from api.models.profile import Profile
from api.serializers.profession import ProfessionSerializer
from api.serializers.address import AddressSerializer
from api.serializers.plan import PlanSerializer


class ProfileSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = "__all__"
        read_only_fields = ("uuid, created_at, modified_at",)
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data: dict):
        profile = Profile.objects.create(**validated_data)
        profile.set_password(validated_data.get("password"))
        profile.save()

        return profile

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["profession"] = ProfessionSerializer(instance.profession).data
        data["plan"] = PlanSerializer(instance.plan).data
        data["address"] = (
            AddressSerializer(instance.address).data if instance.address else None
        )

        return data
