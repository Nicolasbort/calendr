from api.constants.appointment import TypeChoices
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.patient import Patient
from api.models.period import Period
from api.models.profile import Profile
from django.db import models


class Appointment(Uuid, Timestamp, SoftDeletable):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="appointments"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments"
    )
    period = models.ForeignKey(
        Period, on_delete=models.CASCADE, related_name="appointment"
    )
    price = models.DecimalField(max_digits=12, decimal_places=2)
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.TextField(max_length=128, null=True, blank=True)
    notify_appointment = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"Appointment - {self.price}"
