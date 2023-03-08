from api.models.plan import Plan
from api.serializers.plan import PlanSerializer
from rest_framework import generics, permissions, viewsets


class PlanViewSet(
    generics.RetrieveAPIView, generics.ListAPIView, viewsets.GenericViewSet
):
    """
    This viewset allows professionals to retrieve or list plans.
    UNSAFE action like create, update and delete, must be called using admin page.
    """

    queryset = Plan.objects.all()
    serializer_class = PlanSerializer
    permission_classes = [permissions.AllowAny]
