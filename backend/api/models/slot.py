from functools import cached_property

from api.constants.slot import WeekDayChoices
from api.models.base_model import BaseModel
from api.models.calendar import Calendar
from api.utils.datetime import diff
from django.db import models


class Slot(BaseModel):
    calendar = models.ForeignKey(
        Calendar,
        on_delete=models.CASCADE,
        related_name="slots",
        db_index=True,
    )
    week_day = models.PositiveSmallIntegerField(choices=WeekDayChoices.choices)
    time_start = models.TimeField()
    time_end = models.TimeField()

    @cached_property
    def duration(self) -> int:
        return diff(self.time_start, self.time_end)

    @cached_property
    def is_full(self) -> bool:
        """
        If the slot if full of appointments
        """
        appointment_durations = 0

        for appointment in self.appointments.all():
            appointment_durations += appointment.duration

        return appointment_durations >= self.duration
