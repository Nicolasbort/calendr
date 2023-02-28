from api.models.address import Address
from api.serializers.city import CitySerializer
from api.utils.serializers import get_serialized_data
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["city"] = get_serialized_data(CitySerializer, instance.city)

        return data
