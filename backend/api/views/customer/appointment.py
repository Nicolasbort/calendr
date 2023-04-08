from api.models.appointment import Appointment
from api.serializers.appointment import AppointmentSerializer
from rest_framework import permissions, viewsets


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Appointment.objects.filter(patient__profile=self.request.user).all()
