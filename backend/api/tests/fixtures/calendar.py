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
def calendar_create_data():
    return {
        "duration": 60,
        "is_active": True,
        "is_default": True,
        "sessions": [
            {"week_day": 1, "time_start": "07:00:00", "time_end": "07:30:00"},
            {"week_day": 1, "time_start": "07:30:00", "time_end": "08:00:00"},
            {"week_day": 1, "time_start": "08:00:00", "time_end": "08:30:00"},
            {"week_day": 1, "time_start": "08:30:00", "time_end": "09:00:00"},
            {"week_day": 1, "time_start": "09:00:00", "time_end": "09:30:00"},
        ],
    }


@pytest.fixture()
def calendar_update_data():
    return {
        "duration": 30,
        "is_active": False,
        "is_default": False,
        "sessions": [
            {"week_day": 3, "time_start": "07:00:00", "time_end": "07:30:00"},
            {"week_day": 3, "time_start": "07:30:00", "time_end": "08:00:00"},
            {"week_day": 4, "time_start": "08:00:00", "time_end": "08:30:00"},
            {"week_day": 4, "time_start": "08:30:00", "time_end": "09:00:00"},
            {"week_day": 5, "time_start": "09:00:00", "time_end": "09:30:00"},
        ],
    }


@pytest.fixture()
def customer_calendar_fields():
    return [
        "id",
        "professional",
        "sessions",
        "period",
        "name",
    ]
