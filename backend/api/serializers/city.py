from api.models.city import City
from api.serializers.generic import ReadOnlySerializer


class CitySerializer(ReadOnlySerializer):
    class Meta:
        model = City
        exclude = (
            "deleted_at",
            "created_at",
            "modified_at",
        )
