from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer, ShowCalendarSerializer
from api.views.generic import ProfessionalAPIView


class CalendarViewSet(ProfessionalAPIView):
    queryset = Calendar.objects.all()

    def get_serializer_class(self):
        return (
            ShowCalendarSerializer
            if self.action == "list" or self.action == "retrieve"
            else CalendarSerializer
        )
