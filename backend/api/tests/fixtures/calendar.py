import pytest
from api.models.calendar import Calendar


@pytest.fixture()
def calendar(profile):
    return Calendar.objects.create(profile=profile)
