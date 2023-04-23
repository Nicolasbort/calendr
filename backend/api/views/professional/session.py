from api.filters.session import SessionFilter
from api.models.session import Session
from api.serializers.session import CreateSessionSerializer, SessionSerializer
from api.views.generic import ProfessionalAPIView


class SessionViewSet(ProfessionalAPIView):
    """
    Viewset to handle sessions of the default professional calendar
    """

    queryset = Session.objects.all()
    serializer_class: SessionSerializer | CreateSessionSerializer
    filterset_class = SessionFilter
    profile_path = "calendar__professional__profile"

    def get_queryset(self):
        queryset = super().get_queryset()

        return queryset.filter(
            calendar__is_active=True,
            calendar__is_default=True,
        )

    def get_serializer_class(self):
        return (
            SessionSerializer
            if self.action in ["list", "retrieve"]
            else CreateSessionSerializer
        )
