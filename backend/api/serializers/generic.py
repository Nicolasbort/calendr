from api.models.patient import Patient
from api.models.professional import Professional
from api.models.profile import Profile
from drf_spectacular.utils import extend_schema_serializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


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
    password = serializers.CharField(required=False)
    username = serializers.CharField(required=False)

    def create(
        self, validated_data: dict, model_class: Professional | Patient
    ) -> Professional | Patient:
        password = validated_data.pop("password", None)
        if password is None:
            ValidationError("password is required")

        instance = model_class()
        profile = Profile(is_staff=False)
        profile.set_password(password)

        for attr, value in validated_data.items():
            if attr in Profile.WRITABLE_KEYS:
                setattr(profile, attr, value)
            else:
                setattr(instance, attr, value)

        instance.profile = profile

        profile.save()
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

        instance.profile = profile

        profile.save()
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
