from api.models.professional import Professional
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseSerializer,
    WriteBaseProfileSerializer,
)
from api.serializers.notification import NotificationSerializer


class ProfessionalSerializer(WriteBaseProfileSerializer, BaseSerializer):
    notifications = NotificationSerializer(read_only=True, many=True)

    class Meta:
        model = Professional
        read_only_fields = (
            "notifications",
            "username",
        ) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "deleted_at",
            "profile",
        )

    def create(self, validated_data: dict) -> Professional:
        profile = self.create_profile(self, validated_data)

        return Professional.objects.create(profile=profile, **validated_data)
