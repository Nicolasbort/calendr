from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from api.views.generic import ProfessionalAPIView


class CalendarViewSet(ProfessionalAPIView):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
