import builtins
import logging
import random
from functools import cached_property

from api.constants.profile import GenreChoices
from api.models.address import Address
from api.models.base_model import BaseModel
from api.models.plan import Plan
from api.models.profession import Profession
from api.models.profile import Profile
from django.db import models

logger = logging.getLogger("django")


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
    username = models.CharField(max_length=64, unique=True, db_index=True)
    registration_number = models.CharField(max_length=32)
    picture = models.CharField(max_length=128, null=True)
    genre = models.CharField(max_length=1, choices=GenreChoices.choices, null=True)
    birthday = models.DateField(null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.full_name

    @builtins.property
    def full_name(self) -> str:
        return self.profile.full_name

    @builtins.property
    def first_name(self) -> str:
        return self.profile.first_name

    @first_name.setter
    def first_name(self, value):
        self.profile.first_name = value

    @builtins.property
    def last_name(self) -> str:
        return self.profile.last_name

    @last_name.setter
    def last_name(self, value):
        self.profile.last_name = value

    @builtins.property
    def email(self) -> str:
        return self.profile.email

    @email.setter
    def email(self, value):
        self.profile.email = value

    @builtins.property
    def phone(self) -> str:
        return self.profile.phone

    @phone.setter
    def phone(self, value):
        self.profile.phone = value

    @builtins.property
    def password(self) -> str:
        return self.profile.password

    @password.setter
    def password(self, value):
        self.profile.set_password(value)

    @builtins.property
    def notifications(self) -> list:
        return self.profile.notifications or []

    def create_username(self):
        attempt = 0
        base_username = self.full_name.lower()
        base_username = base_username.replace(" ", "")
        self.username = base_username

        while Professional.objects.filter(username=self.username).exists():
            attempt += 1

            logger.warn(
                f"Professional insertion attempt {attempt} failed: Username '{self.username}' not unique. Creating another one"
            )

            self.username = base_username + str(random.randint(0, 9999))

    def save(self, *args, **kwargs) -> None:
        if self._state.adding:
            self.create_username()

        super().save(*args, **kwargs)
