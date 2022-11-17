import builtins
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager

from api.constants.profile import GenreChoices
from api.models.base_model import Timestamp, Uuid
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.address import Address


class Profile(AbstractBaseUser, Uuid, Timestamp):
    username = models.CharField(max_length=64, unique=True, db_index=True)
    email = models.CharField(max_length=128, unique=True, db_index=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    picture = models.CharField(max_length=128, null=True)
    password = models.CharField(max_length=255)
    bio = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices)
    birthday = models.DateTimeField(null=True)
    address = models.OneToOneField(Address, on_delete=models.RESTRICT, null=True)
    profession = models.ForeignKey(
        Profession, on_delete=models.RESTRICT, related_name="users"
    )
    plan = models.ForeignKey(Plan, on_delete=models.RESTRICT, related_name="users")

    USERNAME_FIELD = "username"
    objects = UserManager()

    @builtins.property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self) -> str:
        return self.full_name
