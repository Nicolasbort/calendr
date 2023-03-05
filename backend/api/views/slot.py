from api.models.slot import Slot
from api.serializers.slot import SlotSerializer
from rest_framework import viewsets


class SlotViewSet(viewsets.ModelViewSet):
    serializer_class = SlotSerializer
    permission_classes = []

    def get_queryset(self):
        return Slot.objects.filter(calendar=self.kwargs["calendar_pk"])
