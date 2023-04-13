from api.models.professional import Professional
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseProfileSerializer,
    BaseSerializer,
)
from api.serializers.notification import NotificationSerializer


class ProfessionalSerializer(BaseProfileSerializer, BaseSerializer):
    notifications = NotificationSerializer(read_only=True, many=True)

    class Meta:
        model = Professional
        read_only_fields = ("notifications",) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "deleted_at",
            "profile",
        )

    def create(self, validated_data) -> Professional:
        return super().create(validated_data, Professional)
