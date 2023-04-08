from api.models.professional import Professional
from api.serializers.generic import BaseProfileSerializer, BaseSerializer


class ProfessionalSerializer(BaseProfileSerializer, BaseSerializer):
    class Meta:
        model = Professional
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at", "profile")

    def create(self, validated_data) -> Professional:
        return super().create(validated_data, Professional)
