from uuid import UUID

from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer, ListCalendarSerializer
from api.views.professional.base_viewset import BaseViewSet
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status


class CalendarViewSet(BaseViewSet):
    lookup_field = "pk"
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def get_object(self):
        if self.action != "retrieve":
            return super().get_object()

        value = self.kwargs[self.lookup_field]
        filter_kwargs = {self.lookup_field: value}

        try:
            UUID(value)
        except ValueError:
            filter_kwargs = {
                "professional__profile__username": value,
                "is_default": True,
                "is_active": True,
            }

        obj = get_object_or_404(self.queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj
