from datetime import time

import pytest
from api.models.slot import Slot


@pytest.fixture()
def slot(calendar):
    return Slot.objects.create(
        calendar=calendar,
        week_day=1,
        time_start=time(15, 0),
        time_end=time(17, 0),
    )


@pytest.fixture()
def other_slot(calendar):
    return Slot.objects.create(
        calendar=calendar,
        week_day=1,
        time_start=time(19, 0),
        time_end=time(20, 0),
    )


@pytest.fixture()
def admin_slot(admin_calendar):
    return Slot.objects.create(
        calendar=admin_calendar,
        week_day=1,
        time_start=time(15, 0),
        time_end=time(17, 0),
    )
