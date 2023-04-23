import builtins
from functools import cached_property

from api.constants.session import WeekDayChoices
from api.models.base_model import BaseModel
from api.models.calendar import Calendar
from api.models.professional import Professional
from django.db import models


class Session(BaseModel):
    calendar = models.ForeignKey(
        Calendar,
        on_delete=models.CASCADE,
        related_name="sessions",
        db_index=True,
    )
    week_day = models.PositiveSmallIntegerField(choices=WeekDayChoices.choices)
    time_start = models.TimeField()
    time_end = models.TimeField()

    def __str__(self) -> str:
        week_day = WeekDayChoices(self.week_day).label
        time_start = self.time_start.strftime("%H:%M")
        time_end = self.time_end.strftime("%H:%M")

        return f"{week_day} - {time_start} to {time_end}"

    @builtins.property
    def duration(self) -> int:
        return self.calendar.duration

    @cached_property
    def professional(self) -> Professional:
        return self.calendar.professional
