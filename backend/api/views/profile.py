from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer
from rest_framework import permissions, viewsets


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAdminUser]
