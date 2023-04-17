from api.filters.session import SessionFilter
from api.models.session import Session
from api.permissions import IsAdminOrProfessional, IsProfessional
from api.serializers.session import CreateSessionSerializer, SessionSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter


class SessionViewSet(viewsets.ModelViewSet):
    queryset = Session.objects.all()
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

    def get_serializer_class(self):
        return (
            SessionSerializer
            if self.action in ["list", "retrieve"]
            else CreateSessionSerializer
        )


class SessionDefaultViewSet(viewsets.ModelViewSet):
    """
    Viewset to handle sessions of the default professional calendar
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer
    permission_classes = [IsProfessional]
    filterset_class = SessionFilter

    def get_queryset(self):
        return Session.objects.filter(
            calendar__professional__profile=self.request.user,
            calendar__is_active=True,
            calendar__is_default=True,
        ).all()

    def get_serializer_class(self):
        return (
            SessionSerializer
            if self.action in ["list", "retrieve"]
            else CreateSessionSerializer
        )
