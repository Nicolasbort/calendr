from decimal import Decimal
from functools import cached_property

from api.constants.appointment import TypeChoices
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.slot import Slot
from api.utils.datetime import diff
from django.core.validators import MinValueValidator
from django.db import models


class Appointment(Uuid, Timestamp, SoftDeletable):
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_index=True,
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments", db_index=True
    )
    slot = models.ForeignKey(
        Slot, on_delete=models.CASCADE, related_name="appointments"
    )
    time_start = models.TimeField()
    time_end = models.TimeField()
    price = models.DecimalField(
        max_digits=10, decimal_places=2, validators=[MinValueValidator(Decimal("0.00"))]
    )
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.TextField(max_length=128, null=True, blank=True)
    notify_appointment = models.BooleanField(default=True)

    @cached_property
    def duration(self) -> int:
        return diff(self.time_start, self.time_end)
