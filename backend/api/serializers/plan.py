from api.models.plan import Plan
from api.serializers.generic import BaseSerializer


class PlanSerializer(BaseSerializer):
    class Meta:
        model = Plan
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        fields = read_only_fields + ("name",)
