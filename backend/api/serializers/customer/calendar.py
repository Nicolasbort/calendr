import logging

from api.models.calendar import Calendar
from api.serializers.customer.professional import CustomerProfessionalSerializer
from api.serializers.customer.session import CustomerSessionSerializer
from api.serializers.generic import CUSTOMER_HIDDEN_FIELDS, ReadOnlySerializer
from api.utils.serializers import get_serialized_data
from rest_framework import serializers

logger = logging.getLogger("django")


class CustomerCalendarSerializer(ReadOnlySerializer):
    professional = CustomerProfessionalSerializer(read_only=True)
    sessions = CustomerSessionSerializer(many=True)
    period = serializers.IntegerField(read_only=True)

    class Meta:
        model = Calendar
        exclude = (
            "is_default",
            "is_active",
            "duration",
            "interval",
        ) + CUSTOMER_HIDDEN_FIELDS

    def to_representation(self, instance):
        data = super().to_representation(instance)

        session_serializer = CustomerSessionSerializer(
            data=instance.sessions.all().order_by("week_day", "time_start"), many=True
        )
        session_serializer.is_valid()

        data["sessions"] = session_serializer.data
        data["professional"] = get_serialized_data(
            CustomerProfessionalSerializer, instance.professional
        )

        return data
