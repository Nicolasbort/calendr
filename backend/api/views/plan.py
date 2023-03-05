from api.models.plan import Plan
from api.serializers.plan import PlanSerializer
from rest_framework import permissions, viewsets


class PlanViewSet(viewsets.ModelViewSet):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.IsAdminUser]
