from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework import viewsets, status
from rest_framework.response import Response

from api.serializers.profile import ProfileSerializer
from api.models.address import Address

User = get_user_model()


class SignUpViewSet(viewsets.ViewSet):
    permission_classes = []

    def create(self, request, **_):
        user = User.objects.filter(
            Q(username=request.data.get("username"))
            | Q(email=request.data.get("username"))
        )

        if user.exists():
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"details": "Um usuário com esses dados já existe"},
            )

        address = request.data.pop("address", None)
        if address:
            address = Address.objects.create(**address)

        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save(address=address)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
