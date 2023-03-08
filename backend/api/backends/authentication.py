from typing import Optional
from uuid import UUID

from api.models.profile import Profile
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.base_user import AbstractBaseUser
from django.db.models import Q


class CustomAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            profile = Profile.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except Profile.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            Profile().set_password(password)
        else:
            if profile.check_password(password) and self.user_can_authenticate(profile):
                return profile

    def get_user(self, user_id: str | UUID) -> Optional[AbstractBaseUser]:
        try:
            return Profile.objects.get(pk=user_id)
        except Profile.DoesNotExist:
            return None
