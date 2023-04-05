from api.models.profession import Profession
from api.serializers.profession import ProfessionSerializer
from api.views.generic import SafeAPIView


class ProfessionViewSet(SafeAPIView):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
