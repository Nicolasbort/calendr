from api.models.period import Period
from api.serializers.period import PeriodSerializer
from rest_framework import viewsets


class PeriodViewSet(viewsets.ModelViewSet):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer
    permission_classes = []
