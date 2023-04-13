from api.models.appointment import Appointment
from api.serializers.customer.appointment import (
    CustomerAppointmentSerializer,
    CustomerCreateAppointmentSerializer,
)
from rest_framework import permissions, viewsets


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = CustomerAppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return (
            CustomerAppointmentSerializer
            if self.action in ["list", "retrieve"]
            else CustomerCreateAppointmentSerializer
        )

    def get_queryset(self):
        return Appointment.objects.filter(patient__profile=self.request.user).all()
