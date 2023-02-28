from api.models.patient import Patient
from api.serializers.patient import PatientSerializer
from rest_framework import permissions, viewsets


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(profile=self.request.user).all()
