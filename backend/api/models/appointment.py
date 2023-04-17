import builtins

from api.constants.appointment import TypeChoices
from api.constants.notification import TypeChoices as NotificationTypeChoices
from api.models.base_model import BaseModel
from api.models.patient import Patient
from api.models.professional import Professional
from api.models.session import Session
from api.tasks.notification import create_notification
from django.db import models


class Appointment(BaseModel):
    patient = models.ForeignKey(
        Patient,
        on_delete=models.CASCADE,
        related_name="appointments",
        db_index=True,
    )
    session = models.ForeignKey(
        Session,
        on_delete=models.CASCADE,
        related_name="appointments",
    )
    date = models.DateField()
    type = models.CharField(max_length=16, choices=TypeChoices.choices)
    note = models.CharField(max_length=128, null=True, blank=True)
    link = models.CharField(max_length=255, null=True)
    notify_appointment = models.BooleanField(default=True)

    @builtins.property
    def professional(self) -> Professional:
        return self.session.calendar.professional

    @builtins.property
    def duration(self) -> int:
        return self.session.duration

    def save(self, *args, **kwargs) -> None:
        created = not self.id

        type = NotificationTypeChoices.APPOINTMENT_CREATED
        message = "Uma nova consulta foi agendada"

        if created:
            type = NotificationTypeChoices.APPOINTMENT_UPDATED
            message = "Uma consulta foi alterada"

        create_notification.delay(
            message=message,
            type=type,
            profile_to_id=self.professional.profile.id,
            profile_from_id=self.patient.profile.id,
        )

        return super().save(*args, **kwargs)
