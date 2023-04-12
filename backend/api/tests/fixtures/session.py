from datetime import time

import pytest
from api.models.session import Session


@pytest.fixture()
def session(calendar):
    return Session.objects.create(
        calendar=calendar,
        week_day=1,
        time_start=time(15, 0),
        time_end=time(15, 30),
    )


@pytest.fixture()
def other_session(calendar):
    return Session.objects.create(
        calendar=calendar,
        week_day=1,
        time_start=time(19, 0),
        time_end=time(19, 30),
    )


@pytest.fixture()
def sessions(calendar):
    sessions = [
        Session(
            calendar=calendar,
            week_day=1,
            time_start=time(15, 0),
            time_end=time(15, 30),
        ),
        Session(
            calendar=calendar,
            week_day=1,
            time_start=time(15, 30),
            time_end=time(16, 0),
        ),
        Session(
            calendar=calendar,
            week_day=1,
            time_start=time(16, 0),
            time_end=time(16, 30),
        ),
        Session(
            calendar=calendar,
            week_day=2,
            time_start=time(8, 0),
            time_end=time(8, 30),
        ),
        Session(
            calendar=calendar,
            week_day=2,
            time_start=time(8, 30),
            time_end=time(9, 0),
        ),
    ]
    return Session.objects.bulk_create(sessions)
