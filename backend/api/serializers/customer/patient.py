from api.models.patient import Patient
from api.serializers.customer.professional import CustomerShortProfessionalSerializer
from api.serializers.generic import (
    CUSTOMER_HIDDEN_FIELDS,
    BaseSerializer,
    WriteBaseProfileSerializer,
)


class CustomerPatientSerializer(WriteBaseProfileSerializer, BaseSerializer):
    professional = CustomerShortProfessionalSerializer(read_only=True)

    UPDATE_PROFILE_KEYS = ["first_name", "last_name"]
    READ_PROFILE_KEYS = ["first_name", "last_name", "full_name", "phone", "email"]

    class Meta:
        model = Patient
        read_only_fields = (
            "professional",
            "notify_appointment",
        )
        exclude = (
            "profile",
            "is_confirmed",
            "notify_pending_payment",
        ) + CUSTOMER_HIDDEN_FIELDS
