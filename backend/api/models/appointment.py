from api.constants.appointment import TypeChoices
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.slot import Slot
from django.db import models


class Appointment(Uuid, Timestamp, SoftDeletable):
    professional = models.ForeignKey(
        Professional, on_delete=models.CASCADE, related_name="appointments"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments"
    )
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, related_name="appointment")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.TextField(max_length=128, null=True, blank=True)
    notify_appointment = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Appointment - {self.price}"
