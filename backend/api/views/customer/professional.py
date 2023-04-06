from api.models.calendar import Calendar
from api.models.professional import Professional
from api.serializers.calendar import ShowCalendarSerializer
from api.serializers.professional import ProfessionalSerializer
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ProfessionalViewSet(generics.RetrieveAPIView, viewsets.GenericViewSet):
    lookup_field = "username"
    serializer_class = ProfessionalSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Professional.objects.filter(
            profile__username=self.kwargs.get("username")
        )

    def get_object(self):
        obj = get_object_or_404(self.get_queryset())

        self.check_object_permissions(self.request, obj)

        return obj

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
