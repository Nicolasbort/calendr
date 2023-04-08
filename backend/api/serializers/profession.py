from api.models.profession import Profession
from api.serializers.generic import BaseSerializer


class ProfessionSerializer(BaseSerializer):
    class Meta:
        model = Profession
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        fields = read_only_fields + ("name",)
