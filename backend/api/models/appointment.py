from decimal import Decimal
from functools import cached_property

from api.constants.appointment import TypeChoices
from api.models.base_model import BaseModel
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.slot import Slot
from api.utils.datetime import diff
from django.core.validators import MinValueValidator
from django.db import models


class Appointment(BaseModel):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_index=True,
    )
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_index=True,
    )
    slot = models.ForeignKey(
        Slot,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal("0.00"))],
    )
    time_start = models.TimeField()
    time_end = models.TimeField()
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.CharField(max_length=128, null=True, blank=True)
    link = models.CharField(max_length=255, null=True)
    notify_appointment = models.BooleanField(default=True)

    @cached_property
    def duration(self) -> int:
        return diff(self.time_start, self.time_end)
