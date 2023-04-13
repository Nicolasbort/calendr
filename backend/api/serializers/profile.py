from api.models.profile import Profile
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseSerializer,
    ReadOnlySerializer,
)
from rest_framework import serializers


class ProfileSerializer(ReadOnlySerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        read_only_fields = ("notifications",) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "modified_at",
            "deleted_at",
            "password",
            "last_login",
            "is_superuser",
            "is_staff",
            "groups",
            "user_permissions",
        )


class CreateProfileSerializer(BaseSerializer):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        read_only_fields = ("notifications",) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "deleted_at",
            "is_superuser",
            "is_staff",
        )
        extra_kwargs = {"password": {"write_only": True, "min_length": 4}}

    def create(self, validated_data: dict):
        profile = Profile(**validated_data)
        profile.set_password(validated_data.get("password"))
        profile.save()

        return profile
