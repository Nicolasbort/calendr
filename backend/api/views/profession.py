from api.models.profession import Profession
from api.serializers.profession import ProfessionSerializer
from rest_framework import permissions, viewsets


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer
    permission_classes = [permissions.IsAdminUser]
