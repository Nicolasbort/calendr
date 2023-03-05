import pytest
from api.models.calendar import Calendar


@pytest.fixture()
def calendar(profile):
    return Calendar.objects.create(profile=profile)


@pytest.fixture()
def calendar_create_data():
    return {
        "duration": 60,
        "is_default": True,
        "slots": [
            {"date": "2023-01-01", "time_start": "08:00:00", "time_finish": "11:00:00"},
            {"date": "2023-01-01", "time_start": "13:00:00", "time_finish": "17:00:00"},
            {"date": "2023-01-02", "time_start": "07:00:00", "time_finish": "12:00:00"},
            {"date": "2023-01-02", "time_start": "13:30:00", "time_finish": "18:00:00"},
            {"date": "2023-01-03", "time_start": "12:00:00", "time_finish": "19:00:00"},
        ],
    }


@pytest.fixture()
def calendar_update_data():
    return {
        "duration": 30,
        "is_default": False,
        "slots": [
            {"date": "2023-01-03", "time_start": "07:00:00", "time_finish": "12:00:00"},
            {"date": "2023-01-03", "time_start": "13:30:00", "time_finish": "18:00:00"},
            {"date": "2023-01-04", "time_start": "07:00:00", "time_finish": "12:00:00"},
            {"date": "2023-01-04", "time_start": "13:30:00", "time_finish": "18:00:00"},
            {"date": "2023-01-05", "time_start": "12:00:00", "time_finish": "19:00:00"},
        ],
    }
