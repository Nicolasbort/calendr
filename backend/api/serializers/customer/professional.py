from api.models.professional import Professional
from api.serializers.customer.address import CustomerAddressSerializer
from api.serializers.customer.profession import CustomerProfessionSerializer
from api.serializers.generic import (
    CUSTOMER_HIDDEN_FIELDS,
    ReadOnlySerializer,
    WriteBaseProfileSerializer,
)
from rest_framework import serializers


class CustomerProfessionalSerializer(WriteBaseProfileSerializer, ReadOnlySerializer):
    full_name = serializers.ReadOnlyField()
    address = CustomerAddressSerializer()
    profession = CustomerProfessionSerializer()

    class Meta:
        model = Professional
        depth = 1
        exclude = (
            "profile",
            "plan",
        ) + CUSTOMER_HIDDEN_FIELDS


class CustomerShortProfessionalSerializer(
    WriteBaseProfileSerializer, ReadOnlySerializer
):
    full_name = serializers.ReadOnlyField()

    class Meta:
        model = Professional
        exclude = (
            "profile",
            "plan",
        ) + CUSTOMER_HIDDEN_FIELDS
