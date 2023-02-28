from django.contrib.auth import get_user_model

from rest_framework import viewsets, status, permissions
from rest_framework.response import Response

from api.serializers.profile import ProfileSerializer
from api.serializers.address import AddressSerializer

User = get_user_model()


class SignUpViewSet(viewsets.ViewSet):
    permission_classes = [permissions.AllowAny]

    def create(self, request, **_):
        address = request.data.pop("address", None)
        if address:
            address_serializer = AddressSerializer(data=address)
            address_serializer.is_valid(raise_exception=True)
            address = address_serializer.save()

        serializer = ProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(address=address)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
