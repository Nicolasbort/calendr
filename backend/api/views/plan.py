from rest_framework import viewsets

from api.models.plan import Plan
from api.serializers.plan import PlanSerializer


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = []
