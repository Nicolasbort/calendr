from rest_framework import viewsets

from api.models.profile import Profile
from api.serializers.profile import ProfileSerializer


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
