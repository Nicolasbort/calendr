from api.models.base_model import BaseModel
from api.models.profile import Profile
from django.db import models


class Notification(BaseModel):
    profile_from = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="sent_notifications",
        null=True,
    )
    profile_to = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="received_notifications"
    )
    data = models.JSONField()
    read_at = models.DateTimeField(null=True)
