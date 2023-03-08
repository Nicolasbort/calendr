from api.models import Patient, Profile
from rest_framework import serializers
from rest_framework.fields import SkipField
from rest_framework.relations import PKOnlyObject


class PatientSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField(required=False)

    class Meta:
        model = Patient
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
            "profile",
        )
        exclude = ("deleted_at",)

    def create(self, validated_data):
        profile = Profile(is_staff=False)
        patient = Patient()

        for attr, value in validated_data.items():
            if attr in Profile.WRITABLE_KEYS:
                setattr(profile, attr, value)
            else:
                setattr(patient, attr, value)

        patient.profile = profile

        profile.save()
        patient.save()

        return patient

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

        data["first_name"] = profile.first_name
        data["last_name"] = profile.last_name
        data["email"] = profile.email
        data["phone"] = profile.phone

        return data
