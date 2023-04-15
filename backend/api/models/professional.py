from functools import cached_property

from api.constants.profile import GenreChoices
from api.models.address import Address
from api.models.base_model import BaseModel
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.profile import Profile
from django.db import models


class Professional(BaseModel):
    profession = models.ForeignKey(
        Profession,
        on_delete=models.RESTRICT,
        related_name="professionals",
        db_index=True,
    )
    plan = models.ForeignKey(
        Plan,
        on_delete=models.RESTRICT,
        related_name="professionals",
        db_index=True,
    )
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="professional",
        db_index=True,
    )
    address = models.OneToOneField(
        Address,
        on_delete=models.RESTRICT,
        related_name="professional",
        null=True,
    )
    registration_number = models.CharField(max_length=32)
    picture = models.CharField(max_length=128, null=True)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices, null=True)
    birthday = models.DateField(null=True)
    bio = models.TextField(null=True, blank=True)

    @cached_property
    def full_name(self) -> str:
        return self.profile.full_name

    @cached_property
    def username(self) -> str:
        return self.profile.username

    @cached_property
    def email(self) -> str:
        return self.profile.email

    @cached_property
    def notifications(self) -> list:
        return self.profile.notifications or []

    def __str__(self) -> str:
        return self.full_name
