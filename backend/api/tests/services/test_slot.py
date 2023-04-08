from datetime import time

import pytest
from api.services.slot import split_slots_into_periods
from api.typings.period import Period


@pytest.mark.django_db
class TestSlotService:
    @staticmethod
    def test_split_slots_into_periods(slot):
        expected_periods = {
            1: [
                Period(time_start=time(15, 0), time_end=time(15, 30)),
                Period(time_start=time(15, 30), time_end=time(16, 0)),
                Period(time_start=time(16, 0), time_end=time(16, 30)),
                Period(time_start=time(16, 30), time_end=time(17, 0)),
            ]
        }

        periods = split_slots_into_periods([slot], 30)

        assert expected_periods == periods

    @staticmethod
    def test_split_slots_into_periods_multiple_slots(slot, other_slot):
        expected_periods = {
            1: [
                Period(time_start=time(15, 0), time_end=time(15, 30)),
                Period(time_start=time(15, 30), time_end=time(16, 0)),
                Period(time_start=time(16, 0), time_end=time(16, 30)),
                Period(time_start=time(16, 30), time_end=time(17, 0)),
                Period(time_start=time(19, 0), time_end=time(19, 30)),
                Period(time_start=time(19, 30), time_end=time(20, 0)),
            ]
        }

        periods = split_slots_into_periods([slot, other_slot], 30)

        assert expected_periods == periods

    @staticmethod
    def test_split_slots_into_periods_multiple_slots_different_days(slot, other_slot):
        other_slot.week_day = 3

        expected_periods = {
            1: [
                Period(time_start=time(15, 0), time_end=time(15, 30)),
                Period(time_start=time(15, 30), time_end=time(16, 0)),
                Period(time_start=time(16, 0), time_end=time(16, 30)),
                Period(time_start=time(16, 30), time_end=time(17, 0)),
            ],
            3: [
                Period(time_start=time(19, 0), time_end=time(19, 30)),
                Period(time_start=time(19, 30), time_end=time(20, 0)),
            ],
        }

        periods = split_slots_into_periods([slot, other_slot], 30)

        assert expected_periods == periods
