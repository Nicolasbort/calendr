from api.serializers.profile import ProfileSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class LoggedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        serializer = ProfileSerializer(instance=request.user)

        return Response(status=status.HTTP_200_OK, data=serializer.data)
