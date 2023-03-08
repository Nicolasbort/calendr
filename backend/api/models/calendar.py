from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.professional import Professional
from django.db import models


class Calendar(Uuid, Timestamp, SoftDeletable):
    name = models.CharField(max_length=255, null=True)
    duration = models.PositiveSmallIntegerField()
    interval = models.PositiveSmallIntegerField(default=0)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="calendars"
    )

    def __str__(self) -> str:
        return self.name

    class Meta:
        constraints = [
            # The professional can have only one default calendar
            models.UniqueConstraint(
                fields=["professional", "is_default", "is_active"],
                condition=models.Q(deleted_at=None),
                name="professional_default_active",
            ),
        ]
