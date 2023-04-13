from uuid import UUID

from api.models.calendar import Calendar
from api.models.professional import Professional
from api.openapi.parameters.professional import MULTIPLE_LOOKUP_VIEWSET
from api.serializers.customer.calendar import CustomerCalendarSerializer
from api.serializers.customer.professional import CustomerProfessionalSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


@extend_schema(parameters=MULTIPLE_LOOKUP_VIEWSET)
class ProfessionalViewSet(generics.RetrieveAPIView, viewsets.GenericViewSet):
    lookup_field = "multiple_lookup_field"
    queryset = Professional.objects.all()
    serializer_class = CustomerProfessionalSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        value = self.kwargs[self.lookup_field]

        try:
            UUID(value)

            filter_kwargs = {"pk": value}
        except ValueError:
            filter_kwargs = {"profile__username": value}

        obj = get_object_or_404(self.queryset, **filter_kwargs)

        self.check_object_permissions(self.request, obj)

        return obj

    @extend_schema(responses=CustomerCalendarSerializer)
    @action(methods=["GET"], detail=True, url_path="calendar")
    def get_calendar_default(self, request, *args, **kwargs):
        professional = self.get_object()

        qs = Calendar.objects.filter(
            professional=professional,
            is_active=True,
            is_default=True,
        )

        calendar = get_object_or_404(qs)

        serializer = CustomerCalendarSerializer(calendar)

        return Response(serializer.data)
