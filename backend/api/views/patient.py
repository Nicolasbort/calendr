from api.models.patient import Patient
from api.permissions.is_admin_or_professional import IsAdminOrProfessional
from api.serializers.patient import PatientSerializer
from rest_framework import viewsets


class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    permission_classes = [IsAdminOrProfessional]

    def get_queryset(self):
        if self.request.user.is_staff:
            return Patient.objects.all()

        return Patient.objects.filter(professional__profile=self.request.user)
