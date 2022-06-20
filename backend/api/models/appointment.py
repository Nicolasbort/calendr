import builtins
from django.db import models

from api.constants.appointment import TypeChoices
from api.models.base_model import SoftDeletable, Timestamp, Uuid
from api.models.profile import Profile
from api.models.patient import Patient


class Appointment(Uuid, Timestamp, SoftDeletable):
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="appointments"
    )
    patient = models.ForeignKey(
        Patient, on_delete=models.CASCADE, related_name="appointments"
    )
    date = models.DateTimeField()
    price = models.DecimalField(max_digits=12, decimal_places=2)
    duration = models.PositiveIntegerField()
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.TextField(max_length=128, null=True, blank=True)
    notify_appointment = models.BooleanField(default=True)
