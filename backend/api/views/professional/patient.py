from api.filters.patient import PatientFilter
from api.models.patient import Patient
from api.serializers.patient import PatientSerializer
from api.views.generic import ProfessionalAPIView
from django_filters.rest_framework import DjangoFilterBackend


class PatientViewSet(ProfessionalAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = PatientFilter
