from api.models.appointment import Appointment
from api.permissions import IsAdminOrProfessional
from api.serializers.appointment import (
    AppointmentSerializer,
    CreateAppointmentSerializer,
)
from rest_framework import filters, viewsets


class AppointmentViewSet(viewsets.ModelViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
    permission_classes = [IsAdminOrProfessional]
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        "session__week_day",
        "session__time_start",
    )
    ordering = (
        "session__week_day",
        "session__time_start",
    )

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(
            session__calendar__professional__profile=self.request.user.id
        ).all()

    def get_serializer_class(self):
        return (
            AppointmentSerializer
            if self.action in ["list", "retrieve"]
            else CreateAppointmentSerializer
        )
