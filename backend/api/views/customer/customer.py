from api.models.patient import Patient
from api.serializers.customer.patient import CustomerPatientSerializer
from django.shortcuts import get_object_or_404
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class CustomerViewSet(viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = CustomerPatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Patient.objects.filter(profile=self.request.user)

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())

        obj = get_object_or_404(queryset)

        self.check_object_permissions(self.request, obj)

        return obj

    @action(methods=["GET", "PATCH"], detail=False, url_path="me")
    def me(self, request, *args, **kwargs):
        instance = self.get_object()

        if request.method == "GET":
            return self._retrieve(instance)

        return self._update(instance, request)

    def _update(self, instance, request):
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def _retrieve(self, instance):
        serializer = self.get_serializer(instance)

        return Response(serializer.data)
