from api.constants.notification import TypeChoices
from api.models.notification import Notification
from api.serializers.generic import DEFAULT_READ_ONLY_FIELDS, BaseSerializer
from api.serializers.profile import ProfileSerializer
from rest_framework import serializers


class NotificationDataSerializer(serializers.Serializer):
    message = serializers.CharField()
    type = serializers.ChoiceField(TypeChoices.choices)

    class Meta:
        read_only_fields = (
            "message",
            "type",
        )


class NotificationSerializer(BaseSerializer):
    data = NotificationDataSerializer()
    profile_from = ProfileSerializer()

    class Meta:
        model = Notification
        depth = 1
        read_only_fields = (
            "read_at",
            "profile_from",
            "data",
        ) + DEFAULT_READ_ONLY_FIELDS
        exclude = (
            "profile_to",
            "deleted_at",
        )


class NotificationManySerializer(serializers.Serializer):
    ids = serializers.ListField(child=serializers.UUIDField(), source="")
