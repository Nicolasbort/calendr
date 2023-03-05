from datetime import date, datetime
from functools import cached_property

from api.models.base_model import Timestamp, Uuid
from api.models.calendar import Calendar
from django.db import models


class Slot(Uuid, Timestamp):
    calendar = models.ForeignKey(
        Calendar, on_delete=models.CASCADE, related_name="slots", null=True
    )
    date = models.DateField()
    time_start = models.TimeField()
    time_finish = models.TimeField()

    @cached_property
    def duration(self) -> int:
        """
        Time in minutes of the calendar slot
        """
        datetime_finish = datetime.combine(date.today(), self.time_finish)
        datetime_start = datetime.combine(date.today(), self.time_start)

        diff = datetime_finish - datetime_start

        return round(diff.total_seconds() / 60)
