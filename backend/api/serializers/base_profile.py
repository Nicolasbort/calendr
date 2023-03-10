from api.models.patient import Patient
from api.models.professional import Professional
from api.models.profile import Profile
from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


class BaseProfileSerializer(serializers.ModelSerializer):
    """
    Base profile to abstract profile object in professional and patient serializers
    """

    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    username = serializers.CharField()
    phone = serializers.CharField(required=False)

    def create(
        self, validated_data: dict, model_class: Professional | Patient
    ) -> Professional | Patient:
        profile = Profile(is_staff=False)
        model = model_class()

        for attr, value in validated_data.items():
            if attr in Profile.WRITABLE_KEYS:
                setattr(profile, attr, value)
            else:
                setattr(model, attr, value)

        model.profile = profile

        profile.save()
        model.save()

        return model

    def update(self, instance, validated_data: dict):
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
