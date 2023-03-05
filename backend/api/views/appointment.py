from api.models.appointment import Appointment
from api.permissions.is_admin_or_professional import IsAdminOrProfessional
from api.serializers.appointment import AppointmentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    permission_classes = [IsAdminOrProfessional]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ("patient__id",)

    def get_queryset(self):
        if self.request.user.is_staff:
            return Appointment.objects.all()

        return Appointment.objects.filter(professional__profile=self.request.user).all()
