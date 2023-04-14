import builtins
import logging
import random

from api.models.base_model import BaseModel
from api.models.calcs import profile as profile_calcs
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models

logger = logging.getLogger("django")


class Profile(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    username = models.CharField(max_length=64, unique=True, db_index=True)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=32, null=True, unique=True)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = []
    WRITABLE_KEYS = [
        "first_name",
        "last_name",
        "email",
        "username",
        "phone",
    ]
    objects = UserManager()

    def __str__(self) -> str:
        return self.full_name

    @builtins.property
    def full_name(self) -> str:
        return profile_calcs.full_name(self)

    @builtins.property
    def is_active(self) -> bool:
        return True

    def generate_token(self) -> str:
        return profile_calcs.generate_token(self)

    def verify_token(self, token: str) -> bool:
        return profile_calcs.verify_token(self, token)

    def create_username(self):
        attempt = 0
        base_username = self.first_name.lower() + self.last_name.lower()
        base_username = base_username.replace(" ", "")
        self.username = base_username

        while Profile.objects.filter(username=self.username).exists():
            attempt += 1

            logger.warn(
                f"Profile insertion attempt {attempt} failed: Username '{self.username}' not unique. Creating another one"
            )

            self.username = base_username + str(random.randint(0, 9999))
