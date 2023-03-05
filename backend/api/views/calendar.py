from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from rest_framework import permissions, viewsets


class CalendarViewSet(viewsets.ModelViewSet):
    serializer_class = CalendarSerializer
    permission_classes = [permissions.IsAdminUser]
