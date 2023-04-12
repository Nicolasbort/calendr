import builtins
from decimal import Decimal

from api.constants.appointment import TypeChoices
from api.models.base_model import BaseModel
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.session import Session
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
    session = models.OneToOneField(
        Session,
        on_delete=models.CASCADE,
        related_name="appointment",
    )
    date = models.DateField()
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.CharField(max_length=128, null=True, blank=True)
    link = models.CharField(max_length=255, null=True)
    notify_appointment = models.BooleanField(default=True)

    @builtins.property
    def duration(self) -> int:
        return self.session.duration
