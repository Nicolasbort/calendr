from api.models.payment import Payment
from rest_framework import serializers


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)
