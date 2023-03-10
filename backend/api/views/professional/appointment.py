from api.models.appointment import Appointment
from api.serializers.appointment import AppointmentSerializer
from api.views.professional.base_viewset import BaseViewSet


class AppointmentViewSet(BaseViewSet):
    serializer_class = AppointmentSerializer
    queryset = Appointment.objects.all()
