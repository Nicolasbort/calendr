from api.models.payment import Payment
from api.serializers.payment import PaymentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAdminUser]
    filter_backends = (DjangoFilterBackend,)
