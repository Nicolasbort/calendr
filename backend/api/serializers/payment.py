from rest_framework import serializers

from api.models.payment import Payment


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = "__all__"
        read_only_fields = (
            "uuid",
            "created_at",
            "modified_at",
        )
