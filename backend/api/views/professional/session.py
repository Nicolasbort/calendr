from api.models.session import Session
from api.serializers.session import SessionSerializer
from api.views.generic import ProfessionalAPIView


class SessionViewSet(ProfessionalAPIView):
    queryset = Session.objects.all()
    serializer_class = SessionSerializer

    def get_queryset(self):
        """
        This is a nested route, so we always get by the calendar
        """
        self.queryset = Session.objects.filter(
            calendar=self.kwargs["calendar_pk"]
        ).all()

        return super().get_queryset()
