from api.models.profile import Profile
from api.serializers.generic import BaseSerializer
from rest_framework import serializers


class ProfileSerializer(BaseSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = (
            "deleted_at",
            "is_staff",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data: dict):
        profile = Profile(**validated_data)
        profile.set_password(validated_data.get("password"))
        profile.save()

        return profile
