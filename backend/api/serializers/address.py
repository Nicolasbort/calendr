from api.models.address import Address
from api.serializers.city import CitySerializer
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseSerializer,
    ReadOnlySerializer,
)
from rest_framework.serializers import CharField


class AddressSerializer(ReadOnlySerializer):
    full_address = CharField(read_only=True)

    class Meta:
        model = Address
        depth = 1
        exclude = ("deleted_at",)


class CreateAddressSerializer(BaseSerializer):
    full_address = CharField(read_only=True)
    city = CitySerializer()

    class Meta:
        model = Address
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        exclude = ("deleted_at",)

    def create(self, validated_data):
        city = validated_data.pop("city")

        city_serializer = CitySerializer(data=city)
        city_serializer.is_valid(raise_exception=True)

        validated_data["city"] = city_serializer.save()

        return super().create(validated_data)
