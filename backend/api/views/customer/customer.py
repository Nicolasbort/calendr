from api.models.patient import Patient
from api.serializers.customer.patient import CustomerPatientSerializer
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CustomerViewSet(viewsets.GenericViewSet):
    serializer_class = CustomerPatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(profile=self.request.user)

    @action(methods=["GET"], detail=False, url_path="me")
    def me(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
