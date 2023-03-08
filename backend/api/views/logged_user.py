from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView


class LoggedUserView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs):
        try:
            serializer = ProfileSerializer(Profile.objects.get(pk=request.user.id))
        except Profile.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={
                    "error": "User not found. This error may happen if the user was deleted"
                },
            )

        return Response(status=status.HTTP_200_OK, data=serializer.data)
