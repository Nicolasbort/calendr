import pytest
from api.models.calendar import Calendar


@pytest.fixture()
def calendar(profile):
    return Calendar.objects.create(profile=profile)


@pytest.fixture()
def calendar_create_data(profile):
    return {
        "profile": str(profile.id),
        "periods": [
            {
                "date_start": "2023-01-01 07:00:00",
                "date_finish": "2023-01-01 07:30:00",
            },
            {
                "date_start": "2023-01-01 07:30:00",
                "date_finish": "2023-01-01 08:00:00",
            },
            {
                "date_start": "2023-01-02 07:00:00",
                "date_finish": "2023-01-02 07:45:00",
            },
            {
                "date_start": "2023-01-02 14:00:00",
                "date_finish": "2023-01-02 14:35:00",
            },
        ],
    }


@pytest.fixture()
def calendar_update_data(other_profile):
    return {
        "profile": str(other_profile.id),
        "periods": [
            {
                "date_start": "2023-01-03 07:00:00",
                "date_finish": "2023-01-03 07:30:00",
            },
            {
                "date_start": "2023-01-03 10:30:00",
                "date_finish": "2023-01-03 11:00:00",
            },
            {
                "date_start": "2023-02-03 09:00:00",
                "date_finish": "2023-02-03 09:45:00",
            },
            {
                "date_start": "2023-03-01 17:00:00",
                "date_finish": "2023-03-01 17:45:00",
            },
            {
                "date_start": "2023-07-01 20:00:00",
                "date_finish": "2023-07-01 20:45:00",
            },
        ],
    }
