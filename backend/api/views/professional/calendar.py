from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer, CreateCalendarSerializer
from api.views.generic import ProfessionalAPIView
from drf_spectacular.utils import extend_schema
from rest_framework.decorators import action
from rest_framework.response import Response


class CalendarViewSet(ProfessionalAPIView):
    queryset = Calendar.objects.all()
    serializer_class: CalendarSerializer | CreateCalendarSerializer

    def get_serializer_class(self):
        return (
            CalendarSerializer
            if self.action in ["list", "retrieve"]
            else CreateCalendarSerializer
        )

    @extend_schema(responses=CalendarSerializer)
    @action(methods=["GET"], detail=False, url_path="default")
    def get_calendar_default(self, request, *args, **kwargs):
        qs = self.get_queryset()

        calendar = qs.get(
            is_active=True,
            is_default=True,
        )

        serializer = CalendarSerializer(instance=calendar)

        return Response(serializer.data)
