from api.models.city import City
from api.serializers.city import CitySerializer
from rest_framework import viewsets


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = []
