from api.models.patient import Patient
from api.models.professional import Professional
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


class BaseProfileSerializer(serializers.ModelSerializer):
    """
    Base profile to abstract profile object in professional and patient serializers
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    password = serializers.CharField(required=False, write_only=True)
    username = serializers.CharField(read_only=True)

    def create(
        self, validated_data: dict, model_class: Professional | Patient
    ) -> Professional | Patient:
        password = validated_data.pop("password", None)

        if password is None:
            ValidationError("password is required")

        profile = Profile(is_staff=False, is_superuser=False)
        instance = model_class()

        for attr, value in validated_data.items():
            if attr in Profile.WRITABLE_KEYS:
                setattr(profile, attr, value)
            else:
                setattr(instance, attr, value)

        profile.create_username()
        profile.set_password(password)
        profile.save()

        instance.profile = profile
        instance.save()

        return instance

    def update(self, instance, validated_data: dict):
        validated_data.pop("password", None)

        profile = instance.profile

        for attr, value in validated_data.items():
            curr_instance = instance

            if attr in Profile.WRITABLE_KEYS:
                curr_instance = profile

            setattr(curr_instance, attr, value)

        profile.save()

        instance.profile = profile
        instance.save()

        return instance

    def to_representation(self, instance):
        data = {}
        readable_fields = self._readable_fields

        for field in readable_fields:
            if field.field_name in Profile.WRITABLE_KEYS:
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

        for writable_key in Profile.WRITABLE_KEYS:
            data[writable_key] = getattr(profile, writable_key)

        return data
