from uuid import UUID

from api.models.calendar import Calendar
from api.serializers.calendar import CalendarSerializer
from api.views.professional.base_viewset import BaseViewSet
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status


class CalendarViewSet(BaseViewSet):
    lookup_field = "multiple_lookup_field"
    queryset = Calendar.objects.all()
    serializer_class = CalendarSerializer

    def get_object(self):
        value = self.kwargs[self.lookup_field]

        try:
            UUID(value)

            filter_kwargs = {"pk": value}
        except ValueError:
            filter_kwargs = {
                "professional__profile__username": value,
                "is_default": True,
                "is_active": True,
            }

        obj = get_object_or_404(self.queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj
