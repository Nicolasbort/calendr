import builtins

from api.models.base_model import BaseModel
from api.models.professional import Professional
from django.db import models


class Calendar(BaseModel):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="calendars",
    )
    name = models.CharField(max_length=255, null=True)
    duration = models.PositiveSmallIntegerField()
    interval = models.PositiveSmallIntegerField(default=0)
    is_default = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    def __str__(self) -> str:
        return self.name

    @builtins.property
    def period(self) -> int:
        return self.duration + self.interval

    class Meta:
        constraints = [
            # The professional can have only one default calendar
            models.UniqueConstraint(
                fields=["professional", "is_default", "is_active"],
                condition=models.Q(deleted_at=None),
                name="professional_default_active",
            ),
        ]

    @classmethod
    def unset_default(cls, professional_id: str):
        cls.objects.filter(professional_id=professional_id, is_default=True).update(
            is_default=False
        )

    @classmethod
    def get_default(cls, professional_id: str):
        cls.objects.filter(professional_id=professional_id, is_default=True).first()
