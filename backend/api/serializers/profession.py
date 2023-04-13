from api.models.profession import Profession
from api.serializers.generic import DEFAULT_READ_ONLY_FIELDS, BaseSerializer


class ProfessionSerializer(BaseSerializer):
    class Meta:
        model = Profession
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        fields = read_only_fields + ("name",)
