from api.models.slot import Slot
from api.serializers.slot import SlotSerializer
from api.views.generic import ProfessionalAPIView


class SlotViewSet(ProfessionalAPIView):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer

    def get_queryset(self):
        """
        This is a nested route, so we always get by the calendar
        """
        self.queryset = Slot.objects.filter(calendar=self.kwargs["calendar_pk"]).all()

        return super().get_queryset()
