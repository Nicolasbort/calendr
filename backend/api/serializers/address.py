from rest_framework import serializers

from api.models.address import Address
from api.serializers.city import CitySerializer


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["city"] = CitySerializer(instance.city).data

        return data
