from api.models.professional import Professional
from api.serializers.base_profile import BaseProfileSerializer


class ProfessionalSerializer(BaseProfileSerializer):
    class Meta:
        model = Professional
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
            "profile",
        )
        exclude = ("deleted_at",)

    def create(self, validated_data) -> Professional:
        return super().create(validated_data, Professional)
