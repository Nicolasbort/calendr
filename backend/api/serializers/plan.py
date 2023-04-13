from api.models.plan import Plan
from api.serializers.generic import DEFAULT_READ_ONLY_FIELDS, BaseSerializer


class PlanSerializer(BaseSerializer):
    class Meta:
        model = Plan
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        fields = read_only_fields + ("name",)
