from api.permissions.belongs_to_professional import BelongsToProfessional
from api.permissions.is_admin_or_professional import IsAdminOrProfessional
from rest_framework import generics, permissions, viewsets


class SafeAPIView(
    generics.RetrieveAPIView, generics.ListAPIView, viewsets.GenericViewSet
):
    """
    This viewset allows professionals to retrieve or list professions.
    UNSAFE actions like create, update and delete, must be called using admin page.
    """

    permission_classes = [permissions.AllowAny]


class ProfessionalAPIView(viewsets.ModelViewSet):
    permission_classes = [IsAdminOrProfessional, BelongsToProfessional]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(professional__profile=self.request.user).all()
