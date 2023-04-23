import builtins

from api.models.base_model import BaseModel
from api.models.calcs import profile as profile_calcs
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.hashers import is_password_usable
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class Profile(AbstractBaseUser, PermissionsMixin, BaseModel):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=32, null=True, unique=True)
    password = models.CharField(max_length=128, null=True)
    is_staff = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    WRITABLE_KEYS = [
        "first_name",
        "last_name",
        "email",
        "phone",
    ]
    objects = UserManager()

    def __str__(self) -> str:
        return self.full_name

    @builtins.property
    def full_name(self) -> str:
        return profile_calcs.full_name(self)

    def generate_token(self) -> str:
        return profile_calcs.generate_token(self)

    def verify_token(self, token: str) -> bool:
        return profile_calcs.verify_token(self, token)

    def save(self, *args, **kwargs) -> None:
        if not is_password_usable(self.password):
            self.set_password(self.password)

        return super().save(*args, **kwargs)
