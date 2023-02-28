from api.models.appointment import Appointment
from api.serializers.appointment import AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, viewsets


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient__id",)

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user).all()
