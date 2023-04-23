from api.models.profile import Profile
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject

DEFAULT_READ_ONLY_FIELDS = (
    "id",
    "created_at",
    "modified_at",
)
CUSTOMER_HIDDEN_FIELDS = (
    "created_at",
    "modified_at",
    "deleted_at",
)


@extend_schema_serializer(exclude_fields=["deleted_at"])
class ReadOnlySerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        pass

    def update(self, instance, validated_data):
        pass


@extend_schema_serializer(exclude_fields=["deleted_at"])
class BaseSerializer(serializers.ModelSerializer):
    pass


class WriteBaseProfileSerializer(serializers.ModelSerializer):
    """
    Base profile to abstract profile object in professional and patient serializers
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    full_name = serializers.CharField(read_only=True)
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField(required=False, write_only=True)

    UPDATE_PROFILE_KEYS: list[str] = ["phone", "email"]
    CREATE_PROFILE_KEYS: list[str] = ["first_name", "last_name", "phone", "email"]
    READ_PROFILE_KEYS: list[str] = [
        "first_name",
        "last_name",
        "full_name",
        "phone",
        "email",
    ]

    def create_profile(self, validated_data: dict) -> Profile:
        password = self.get_password(validated_data)

        profile = Profile(is_staff=False, is_superuser=False)

        for attr in self.CREATE_PROFILE_KEYS:
            value = validated_data.pop(attr)

            setattr(profile, attr, value)

        profile.set_password(password)
        profile.save()

        return profile

    def get_password(self, validated_data: dict) -> str:
        password = validated_data.pop("password", None)

        if password is None:
            ValidationError("password is required")

        return password

    def update(self, instance, validated_data: dict):
        validated_data.pop("password", None)

        profile = instance.profile

        for attr, value in validated_data.items():
            curr_instance = instance

            if attr in self.UPDATE_PROFILE_KEYS:
                curr_instance = profile

            setattr(curr_instance, attr, value)

        instance.profile = profile
        instance.save()

        return instance

    def to_representation(self, instance):
        data = {}
        readable_fields = self._readable_fields

        for field in readable_fields:
            if field.field_name in self.READ_PROFILE_KEYS:
                continue

            try:
                attribute = field.get_attribute(instance)
            except SkipField:
                continue

            check_for_none = (
                attribute.pk if isinstance(attribute, PKOnlyObject) else attribute
            )
            if check_for_none is None:
                data[field.field_name] = None
            else:
                data[field.field_name] = field.to_representation(attribute)

        profile = instance.profile

        for writable_key in self.READ_PROFILE_KEYS:
            data[writable_key] = getattr(profile, writable_key)

        return data
