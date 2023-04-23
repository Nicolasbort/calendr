import builtins

from api.models.base_model import BaseModel
from api.models.calcs import profile as profile_calcs
from api.models.professional import Professional
from api.models.profile import Profile
from django.db import models
from django.db.transaction import atomic


class Patient(BaseModel):
    profile = models.OneToOneField(
        Profile,
        on_delete=models.CASCADE,
        related_name="patient",
        db_index=True,
    )
    professional = models.ForeignKey(
        Professional,
        on_delete=models.CASCADE,
        related_name="patients",
        db_index=True,
    )
    notify_appointment = models.BooleanField(default=True)
    notify_pending_payment = models.BooleanField(default=True)

    # Duplicated values with Profile to allow the Professional to customize the name and not affect the patient itself (Profile)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)

    # If the patient has accepted to be a patient of the Professional that made the request
    is_confirmed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.first_name

    @builtins.property
    def full_name(self) -> str:
        return profile_calcs.full_name(self)

    @builtins.property
    def email(self) -> str:
        return self.profile.email

    @email.setter
    def email(self, value):
        self.profile.email = value

    @builtins.property
    def phone(self) -> str:
        return self.profile.phone

    @phone.setter
    def phone(self, value):
        self.profile.phone = value

    @builtins.property
    def password(self) -> str:
        return self.profile.password

    @password.setter
    def password(self, value):
        self.profile.set_password(value)

    @atomic
    def save(self, *args, **kwargs) -> None:
        self.profile.save()

        return super().save(*args, **kwargs)
