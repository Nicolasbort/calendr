from api.models.session import Session
from api.permissions import IsAdminOrProfessional
from api.serializers.session import SessionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsAdminOrProfessional]
    filter_backends = (
        DjangoFilterBackend,
        OrderingFilter,
    )
    filterset_fields = ("week_day",)
    ordering_fields = (
        "week_day",
        "time_start",
    )
    ordering = (
        "week_day",
        "time_start",
    )

    def get_queryset(self):
        """
        This is a nested route, so we always get by the calendar
        """
        self.queryset = Session.objects.filter(
            calendar=self.kwargs["calendar_pk"]
        ).all()

        return super().get_queryset()
