from uuid import UUID

from api.models.calendar import Calendar
from api.models.professional import Professional
from api.serializers.calendar import ShowCalendarSerializer
from api.serializers.professional import ProfessionalSerializer
from django.shortcuts import get_object_or_404
from drf_spectacular.types import OpenApiTypes
from drf_spectacular.utils import OpenApiParameter, extend_schema
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


@extend_schema(
    parameters=[
        OpenApiParameter(
            "multiple_lookup_field",
            OpenApiTypes.STR,
            OpenApiParameter.PATH,
            description="UUID or username of the professional",
        )
    ]
)
class ProfessionalViewSet(generics.RetrieveAPIView, viewsets.GenericViewSet):
    lookup_field = "multiple_lookup_field"
    queryset = Professional.objects.all()
    serializer_class = ProfessionalSerializer
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

    @extend_schema(responses=ShowCalendarSerializer)
    @action(methods=["GET"], detail=True, url_path="calendar")
    def get_calendar_default(self, request, *args, **kwargs):
        professional = self.get_object()

        qs = Calendar.objects.filter(
            professional=professional,
            is_active=True,
            is_default=True,
        )

        calendar = get_object_or_404(qs)

        serializer = ShowCalendarSerializer(calendar)

        return Response(serializer.data)
