from api.permissions import BelongsToProfessional, IsAdminOrProfessional
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrProfessional, BelongsToProfessional]
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ("patient__id",)

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(professional__profile=self.request.user).all()
