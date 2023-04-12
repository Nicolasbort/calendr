import builtins

from api.constants.session import WeekDayChoices
from api.models.base_model import BaseModel
from api.models.calendar import Calendar
from api.utils.datetime import diff
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

    @builtins.property
    def duration(self) -> int:
        return diff(self.time_start, self.time_end)

    @builtins.property
    def is_scheduled(self) -> bool:
        try:
            return bool(self.appointment)
        except:
            return False
