from api.models.third_party import ThirdParty
from api.serializers.generic import BaseSerializer


class ThirdPartySerializer(BaseSerializer):
    class Meta:
        model = ThirdParty
        read_only_fields = (
            "id",
            "expire_at",
            "professional",
            "scopes",
            "created_at",
            "modified_at",
        )
        exclude = (
            "access_token",
            "refresh_token",
        )
