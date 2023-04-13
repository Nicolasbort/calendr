from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer, CreateCalendarSerializer
from api.views.generic import ProfessionalAPIView


class CalendarViewSet(ProfessionalAPIView):
    queryset = Calendar.objects.all()

    def get_serializer_class(self):
        return (
            CalendarSerializer
            if self.action in ["list", "retrieve"]
            else CreateCalendarSerializer
        )
