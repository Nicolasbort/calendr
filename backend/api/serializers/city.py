from api.models.city import City
from api.serializers.generic import BaseSerializer


class CitySerializer(BaseSerializer):
    class Meta:
        model = City
        fields = (
            "id",
            "name",
            "state",
        )
