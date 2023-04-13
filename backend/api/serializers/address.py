from api.models.address import Address
from api.serializers.generic import (
    DEFAULT_READ_ONLY_FIELDS,
    BaseSerializer,
    ReadOnlySerializer,
)
from rest_framework import serializers


class AddressSerializer(ReadOnlySerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Address
        depth = 1
        exclude = ("deleted_at",)


class CreateAddressSerializer(BaseSerializer):
    full_address = serializers.CharField(read_only=True)

    class Meta:
        model = Address
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        exclude = ("deleted_at",)
