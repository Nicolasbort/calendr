from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.profile import Profile
from django.db import models


class Calendar(Uuid, Timestamp, SoftDeletable):
    name = models.CharField(max_length=255, null=True)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="calendar"
    )
    duration = models.PositiveSmallIntegerField()
    is_default = models.BooleanField(default=False)

    class Meta:
        # The professional can have only one default calendar
        unique_together = (
            "profile",
            "is_default",
        )
