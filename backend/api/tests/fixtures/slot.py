import pytest
from api.models.slot import Slot


@pytest.fixture()
def slot(calendar):
    return Slot.objects.create(
        calendar=calendar,
        date="2023-01-01",
        time_start="15:00:00",
        time_end="16:00:00",
    )


@pytest.fixture()
def admin_slot(admin_calendar):
    return Slot.objects.create(
        calendar=admin_calendar,
        date="2023-01-01",
        time_start="15:00:00",
        time_end="17:00:00",
    )
