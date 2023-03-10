import pytest
from api.models.calendar import Calendar


@pytest.fixture()
def calendar(professional):
    return Calendar.objects.create(
        duration=30,
        interval=0,
        is_default=True,
        is_active=True,
        professional=professional,
    )


@pytest.fixture()
def calendar_not_default(professional):
    return Calendar.objects.create(
        duration=30,
        interval=0,
        is_default=False,
        is_active=True,
        professional=professional,
    )


@pytest.fixture()
def calendar_not_active(professional):
    return Calendar.objects.create(
        duration=30,
        interval=0,
        is_default=True,
        is_active=False,
        professional=professional,
    )


@pytest.fixture()
def calendar_not_active_and_default(professional):
    return Calendar.objects.create(
        duration=30,
        interval=0,
        is_default=False,
        is_active=False,
        professional=professional,
    )


@pytest.fixture()
def admin_calendar(admin_professional):
    return Calendar.objects.create(
        duration=30,
        interval=0,
        is_default=True,
        is_active=True,
        professional=admin_professional,
    )


@pytest.fixture()
def calendar_create_data():
    return {
        "duration": 60,
        "is_active": True,
        "is_default": True,
        "slots": [
            {"week_day": 1, "time_start": "08:00:00", "time_end": "11:00:00"},
            {"week_day": 1, "time_start": "13:00:00", "time_end": "17:00:00"},
            {"week_day": 2, "time_start": "07:00:00", "time_end": "12:00:00"},
            {"week_day": 2, "time_start": "13:30:00", "time_end": "18:00:00"},
            {"week_day": 3, "time_start": "12:00:00", "time_end": "19:00:00"},
        ],
    }


@pytest.fixture()
def calendar_update_data():
    return {
        "duration": 30,
        "is_active": False,
        "is_default": False,
        "slots": [
            {"week_day": 3, "time_start": "07:00:00", "time_end": "12:00:00"},
            {"week_day": 3, "time_start": "13:30:00", "time_end": "18:00:00"},
            {"week_day": 4, "time_start": "07:00:00", "time_end": "12:00:00"},
            {"week_day": 4, "time_start": "13:30:00", "time_end": "18:00:00"},
            {"week_day": 5, "time_start": "12:00:00", "time_end": "19:00:00"},
        ],
    }
