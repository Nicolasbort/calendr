from api.models.patient import Patient
from api.serializers.customer.professional import CustomerShortProfessionalSerializer
from api.serializers.generic import (
    CUSTOMER_HIDDEN_FIELDS,
    BaseProfileSerializer,
    ReadOnlySerializer,
)


class CustomerPatientSerializer(BaseProfileSerializer, ReadOnlySerializer):
    professional = CustomerShortProfessionalSerializer()

    class Meta:
        model = Patient
        exclude = ("profile",) + CUSTOMER_HIDDEN_FIELDS
