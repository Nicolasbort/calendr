from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from api.serializers.profile import ProfileSerializer
from api.models.profile import Profile


class LoggedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        serializer = ProfileSerializer(
            Profile.objects.filter(id=request.user.id).first()
        )
        return Response(serializer.data)
