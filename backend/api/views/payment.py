from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from api.models.payment import Payment
from api.serializers.payment import PaymentSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("appointment__patient__id",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(
            deleted_at__isnull=True, appointment__profile=self.request.user
        ).all()
