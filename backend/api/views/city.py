from api.models.city import City
from api.serializers.city import CitySerializer
from api.views.generic import SafeAPIView


class CityViewSet(SafeAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
