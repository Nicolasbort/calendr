from api.models.plan import Plan
from api.models.profession import Profession
from api.serializers.address import AddressSerializer
from api.serializers.professional import ProfessionalSerializer
from api.serializers.signup import PatientSignupSerializer
from django.db.transaction import atomic
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class SignUpViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.AllowAny]

    @atomic
    @action(methods=["POST"], detail=False, url_path="professional")
    def professional(self, request, **kwargs):
        address = request.data.pop("address", None)

        if address is not None:
            address_serializer = AddressSerializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address = address_serializer.save()

        plan = Plan.get_free_plan()
        profession = Profession.get_default_profession()

        data = {
            **request.data,
            "profession": profession.id,
            "plan": plan.id,
            "address": address.id if address else None,
        }

        serializer = ProfessionalSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK, data=serializer.data)

    @atomic
    @action(methods=["POST"], detail=False, url_path="patient")
    def patient(self, request, **kwargs):
        serializer = PatientSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_200_OK, data=serializer.data)
