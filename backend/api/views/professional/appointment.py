from api.models.appointment import Appointment
from api.serializers.appointment import AppointmentSerializer
from api.views.generic import ProfessionalAPIView


class AppointmentViewSet(ProfessionalAPIView):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
