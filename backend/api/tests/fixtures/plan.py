import pytest
from api.models.plan import Plan


@pytest.fixture()
def plan():
    return Plan.objects.create(name="Free")
