from api.models.plan import Plan
from api.models.profession import Profession
from api.serializers.signup import PatientSignupSerializer, ProfessionalSignupSerializer
from django.db.transaction import atomic
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class SignUpViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]

    def get_serializer_class(self):
        return (
            ProfessionalSignupSerializer
            if self.action == "professional"
            else PatientSignupSerializer
        )

    @atomic
    @extend_schema(responses=ProfessionalSignupSerializer)
    @action(methods=["POST"], detail=False, url_path="professional")
    def professional(self, request, **kwargs):
        serializer = ProfessionalSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        plan = Plan.get_free_plan()
        profession = Profession.get_default_profession()

        serializer.save(plan=plan, profession=profession)

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @atomic
    @extend_schema(responses=PatientSignupSerializer)
    @action(methods=["POST"], detail=False, url_path="patient")
    def patient(self, request, **kwargs):
        serializer = PatientSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK, data=serializer.data)
