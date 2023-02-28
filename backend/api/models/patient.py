import builtins

from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.profile import Profile
from django.db import models


class Patient(Uuid, Timestamp, SoftDeletable):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32, null=True, blank=True)
    email = models.CharField(max_length=128, null=True, unique=True)
    phone = models.CharField(max_length=32, null=True, unique=True)
    notify_pending_payment = models.BooleanField(default=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="patients", null=True
    )

    @builtins.property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self) -> str:
        return self.full_name
