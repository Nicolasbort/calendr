from api.models.patient import Patient
from api.serializers.patient import PatientSerializer
from api.views.generic import ProfessionalAPIView


class PatientViewSet(ProfessionalAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
