from datetime import time

import pytest
from api.services.slot import divide_slots_by_duration


@pytest.mark.django_db
class TestSlotService:
    @staticmethod
    def test_divide_slots_by_duration(slot):
        expected_periods = {
            1: [
                {
                    "time_start": time(15, 0),
                    "time_end": time(15, 30),
                },
                {
                    "time_start": time(15, 30),
                    "time_end": time(16, 0),
                },
                {
                    "time_start": time(16, 0),
                    "time_end": time(16, 30),
                },
                {
                    "time_start": time(16, 30),
                    "time_end": time(17, 0),
                },
            ]
        }

        periods = divide_slots_by_duration([slot], 30)

        assert expected_periods == periods

    @staticmethod
    def test_divide_slots_by_duration_multiple_slots(slot, other_slot):
        expected_periods = {
            1: [
                {
                    "time_start": time(15, 0),
                    "time_end": time(15, 30),
                },
                {
                    "time_start": time(15, 30),
                    "time_end": time(16, 0),
                },
                {
                    "time_start": time(16, 0),
                    "time_end": time(16, 30),
                },
                {
                    "time_start": time(16, 30),
                    "time_end": time(17, 0),
                },
                {
                    "time_start": time(19, 0),
                    "time_end": time(19, 30),
                },
                {
                    "time_start": time(19, 30),
                    "time_end": time(20, 0),
                },
            ]
        }

        periods = divide_slots_by_duration([slot, other_slot], 30)

        assert expected_periods == periods

    @staticmethod
    def test_divide_slots_by_duration_multiple_slots_different_days(slot, other_slot):
        other_slot.week_day = 3

        expected_periods = {
            1: [
                {
                    "time_start": time(15, 0),
                    "time_end": time(15, 30),
                },
                {
                    "time_start": time(15, 30),
                    "time_end": time(16, 0),
                },
                {
                    "time_start": time(16, 0),
                    "time_end": time(16, 30),
                },
                {
                    "time_start": time(16, 30),
                    "time_end": time(17, 0),
                },
            ],
            3: [
                {
                    "time_start": time(19, 0),
                    "time_end": time(19, 30),
                },
                {
                    "time_start": time(19, 30),
                    "time_end": time(20, 0),
                },
            ],
        }

        periods = divide_slots_by_duration([slot, other_slot], 30)

        assert expected_periods == periods
