from functools import cache
from math import floor

from api.models.slot import Slot
from api.typings.period import Period
from api.utils.datetime import add_minutes_to_time


def split_slots_into_periods(slots: list[Slot], duration: int) -> list[Period]:
    """
    duration: 30
    slot 1: "09:00" -> "11:00" & slot 2: "13:00" -> "14:00"
    returned list: "09:00" -> "09:30", "09:30" -> "10:00", "10:00" -> "10:30", "10:30" -> "11:00" & "13:00" -> "13:30", "13:30" -> "14:00"
    """
    periods: list[Period] = {}

    for slot in slots:
        week_day = slot.week_day

        if week_day not in periods:
            periods[week_day] = []

        divided_periods = split_slot_into_periods(slot, duration)
        periods[week_day].extend(divided_periods)

    return periods


@cache
def split_slot_into_periods(slot: Slot, duration: int) -> list[Period]:
    periods_quantity = floor(slot.duration / duration)
    periods = [0] * periods_quantity

    last_period_end = slot.time_start

    for idx in range(periods_quantity):
        period_start = last_period_end
        period_end = add_minutes_to_time(last_period_end, duration)
        last_period_end = period_end

        periods[idx] = Period(time_start=period_start, time_end=period_end)

    return periods
