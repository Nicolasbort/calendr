from api.models.payment import Payment
from api.serializers.generic import BaseSerializer


class PaymentSerializer(BaseSerializer):
    class Meta:
        model = Payment
        read_only_fields = (
            "id",
            "created_at",
            "modified_at",
        )
        exclude = ("deleted_at",)
