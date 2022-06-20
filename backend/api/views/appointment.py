from datetime import datetime
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, permissions

from api.models.appointment import Appointment
from api.serializers.appointment import AppointmentSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient__id",)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(deleted_at__isnull=True, profile=self.request.user).all()

    def perform_destroy(self, instance):
        return instance.save(deleted_at=datetime.now())
