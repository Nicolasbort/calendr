from api.models.city import City
from api.serializers.generic import CUSTOMER_HIDDEN_FIELDS, ReadOnlySerializer


class CustomerCitySerializer(ReadOnlySerializer):
    class Meta:
        model = City
        exclude = CUSTOMER_HIDDEN_FIELDS
