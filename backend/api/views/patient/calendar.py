from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from rest_framework import generics, permissions


class PatientCalendarViewSet(generics.RetrieveAPIView, generics.ListAPIView):
    serializer_class = CalendarSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Calendar.objects.filter(
            professional__profile=self.kwargs.get("professional_pk"), is_default=True
        )
