import builtins

from api.constants.profile import GenreChoices
from api.models.address import Address
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.plan import Plan
from api.models.profession import Profession
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.db import models


class Profile(AbstractBaseUser, PermissionsMixin, Uuid, Timestamp, SoftDeletable):
    username = models.CharField(max_length=64, unique=True, db_index=True)
    email = models.CharField(max_length=128, unique=True, db_index=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    picture = models.CharField(max_length=128, null=True)
    bio = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    birthday = models.DateTimeField(null=True)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, null=True)
    profession = models.ForeignKey(
        Profession, on_delete=models.RESTRICT, related_name="users"
    )
    plan = models.ForeignKey(Plan, on_delete=models.RESTRICT, related_name="users")
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "username"
    objects = UserManager()

    @builtins.property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self) -> str:
        return self.full_name
