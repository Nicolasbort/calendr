from api.permissions import BelongsToProfessional, IsAdminOrProfessional
from rest_framework import generics, permissions, viewsets


class SafeAPIView(
    generics.RetrieveAPIView, generics.ListAPIView, viewsets.GenericViewSet
):
    """
    This viewset allows anyone to list and retrieve models.
    UNSAFE actions like create, update and delete are not allowed.
    """

    permission_classes = [permissions.AllowAny]


class ProfessionalAPIView(viewsets.ModelViewSet):
    """
    This viewset allows professionals or admins to perform any model action.
    """

    permission_classes = [IsAdminOrProfessional, BelongsToProfessional]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        return self.queryset.filter(professional__profile=self.request.user).all()
