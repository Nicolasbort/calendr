from api.models.profile import Profile
from django.contrib.auth.backends import ModelBackend


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            profile = Profile.objects.get(email__iexact=username)
        except Profile.DoesNotExist:
            return

        if profile.check_password(password) and self.user_can_authenticate(profile):
            return profile
