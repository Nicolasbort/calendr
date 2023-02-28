from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from rest_framework import viewsets


class CalendarViewSet(viewsets.ModelViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer
    permission_classes = []
