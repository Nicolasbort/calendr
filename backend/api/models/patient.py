from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.professional import Professional
from api.models.profile import Profile
from django.db import models


class Patient(Uuid, Timestamp, SoftDeletable):
    notify_pending_payment = models.BooleanField(default=True)
    profile = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="patient", db_index=True
    )
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="patients", db_index=True
    )

    def __str__(self) -> str:
        return self.profile.full_name
