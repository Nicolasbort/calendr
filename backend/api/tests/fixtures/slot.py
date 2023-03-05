import pytest
from api.models.slot import Slot


@pytest.fixture()
def slot(calendar):
    return Slot.objects.create(
        calendar=calendar,
        date_start="2023-12-12 15:00:00",
        date_finish="2023-12-12 16:00:00",
    )
