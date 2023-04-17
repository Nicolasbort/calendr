from api.models.session import Session
from api.serializers.generic import CUSTOMER_HIDDEN_FIELDS, ReadOnlySerializer
from rest_framework import serializers


class CustomerSessionSerializer(ReadOnlySerializer):
    class Meta:
        model = Session
        exclude = ("calendar",) + CUSTOMER_HIDDEN_FIELDS
