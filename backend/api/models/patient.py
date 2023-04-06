from functools import cached_property

from api.models.base_model import BaseModel
from api.models.professional import Professional
from api.models.profile import Profile
from django.db import models


class Patient(BaseModel):
    notify_appointment = models.BooleanField(default=True)
    notify_pending_payment = models.BooleanField(default=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="patient", db_index=True
    )
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="patients", db_index=True
    )

    @cached_property
    def full_name(self) -> str:
        return self.profile.full_name

    def __str__(self) -> str:
        return self.full_name
