from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from rest_framework import viewsets


class NestedCalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    permission_classes = []

    def get_queryset(self):
        return Calendar.objects.filter(
            profile=self.kwargs.get("profile_pk"), is_default=True
        )
