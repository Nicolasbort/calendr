from api.models.city import City
from api.serializers.city import CitySerializer
from rest_framework import generics, permissions, viewsets


class CityViewSet(
    generics.RetrieveAPIView, generics.ListAPIView, viewsets.GenericViewSet
):
    """
    This viewset allows professionals to retrieve or list cities.
    UNSAFE actions like create, update and delete, must be called using admin page.
    """

    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.AllowAny]
