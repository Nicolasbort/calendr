from api.models.address import Address
from api.serializers.city import CitySerializer
from api.serializers.generic import BaseSerializer
from api.utils.serializers import get_serialized_data
from rest_framework import serializers


class AddressSerializer(BaseSerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Address
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)

    def to_representation(self, instance):
        data = super().to_representation(instance)

        data["city"] = get_serialized_data(CitySerializer, instance.city)

        return data
