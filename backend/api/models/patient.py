from functools import cached_property

from api.models.base_model import BaseModel
from api.models.professional import Professional
from api.models.profile import Profile
from django.db import models


class Patient(BaseModel):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="patient",
        db_index=True,
    )
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="patients",
        db_index=True,
    )
    notify_appointment = models.BooleanField(default=True)
    notify_pending_payment = models.BooleanField(default=True)

    @cached_property
    def full_name(self) -> str:
        return self.profile.full_name

    @cached_property
    def username(self) -> str:
        return self.profile.username

    @cached_property
    def email(self) -> str:
        return self.profile.email

    def __str__(self) -> str:
        return self.full_name
