from api.models.payment import Payment
from api.serializers.generic import DEFAULT_READ_ONLY_FIELDS, BaseSerializer


class PaymentSerializer(BaseSerializer):
    class Meta:
        model = Payment
        read_only_fields = DEFAULT_READ_ONLY_FIELDS
        exclude = ("deleted_at",)
