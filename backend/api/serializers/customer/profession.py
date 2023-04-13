from api.models.profession import Profession
from api.serializers.generic import CUSTOMER_HIDDEN_FIELDS, ReadOnlySerializer


class CustomerProfessionSerializer(ReadOnlySerializer):
    class Meta:
        model = Profession
        exclude = CUSTOMER_HIDDEN_FIELDS
