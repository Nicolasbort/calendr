from api.models.address import Address
from api.serializers.customer.city import CustomerCitySerializer
from api.serializers.generic import CUSTOMER_HIDDEN_FIELDS, ReadOnlySerializer


class CustomerAddressSerializer(ReadOnlySerializer):
    city = CustomerCitySerializer()

    class Meta:
        model = Address
        depth = 1
        exclude = CUSTOMER_HIDDEN_FIELDS
