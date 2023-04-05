from api.models.plan import Plan
from api.serializers.plan import PlanSerializer
from api.views.generic import SafeAPIView


class PlanViewSet(SafeAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
