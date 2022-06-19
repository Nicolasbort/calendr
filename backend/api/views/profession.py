from rest_framework import viewsets

from api.models.profession import Profession
from api.serializers.profession import ProfessionSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = []
