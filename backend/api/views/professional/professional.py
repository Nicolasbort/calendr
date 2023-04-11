from uuid import UUID

from api.permissions import BelongsToProfessional, IsAdminOrProfessional
from api.serializers.professional import ProfessionalSerializer
from rest_framework import mixins, viewsets


class ProfessionalViewSet(viewsets.GenericViewSet, mixins.UpdateModelMixin):
    permission_classes = [IsAdminOrProfessional, BelongsToProfessional]
    serializer_class = ProfessionalSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(professional__profile=self.request.user).all()
