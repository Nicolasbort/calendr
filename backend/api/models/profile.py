import builtins

from api.models.base_model import SoftDeletable, Timestamp, Uuid
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class Profile(AbstractBaseUser, PermissionsMixin, Uuid, Timestamp, SoftDeletable):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField(unique=True, db_index=True)
    phone = models.CharField(max_length=32, null=True, unique=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    WRITABLE_KEYS = ["first_name", "last_name", "email", "phone"]
    objects = UserManager()

    @builtins.property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self) -> str:
        return self.full_name
