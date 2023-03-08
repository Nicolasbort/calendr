from api.models.patient import Patient
from api.serializers.patient import PatientSerializer
from api.views.professional.base_viewset import BaseViewSet


class ProfessionalPatientViewSet(BaseViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
