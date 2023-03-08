from api.models.profession import Profession
from api.serializers.profession import ProfessionSerializer
from rest_framework import generics, permissions, viewsets


class ProfessionViewSet(
    generics.RetrieveAPIView, generics.ListAPIView, viewsets.GenericViewSet
):
    """
    This viewset allows professionals to retrieve or list professions.
    UNSAFE actions like create, update and delete, must be called using admin page.
    """

    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [permissions.AllowAny]
