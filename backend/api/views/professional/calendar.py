from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer, ListCalendarSerializer
from api.views.professional.base_viewset import BaseViewSet
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response


class ProfessionalCalendarViewSet(BaseViewSet):
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    @action(methods=["GET"], detail=True, url_path="full-calendar")
    def full_calendar(self, request, **kwargs):
        calendar = self.get_object()

        serializer = ListCalendarSerializer(calendar)

        return Response(data=serializer.data, status=status.HTTP_200_OK)
