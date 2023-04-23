from api.models.appointment import Appointment
from api.serializers.appointment import (
    AppointmentSerializer,
    CreateAppointmentSerializer,
)
from api.views.generic import ProfessionalAPIView
from rest_framework import filters


class AppointmentViewSet(ProfessionalAPIView):
    queryset = Appointment.objects.all()
    serializer_class: AppointmentSerializer | CreateAppointmentSerializer
    profile_path = "session__calendar__professional__profile"
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = (
        "session__week_day",
        "session__time_start",
    )
    ordering = (
        "session__week_day",
        "session__time_start",
    )

    def get_serializer_class(self):
        return (
            AppointmentSerializer
            if self.action in ["list", "retrieve"]
            else CreateAppointmentSerializer
        )
