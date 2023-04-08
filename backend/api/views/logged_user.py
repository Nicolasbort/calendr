from api.serializers.profile import ProfileSerializer
from drf_spectacular.utils import extend_schema
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class LoggedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(responses=ProfileSerializer)
    def get(self, request, **kwargs):
        serializer = ProfileSerializer(instance=request.user)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
