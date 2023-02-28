import pytest
from api.models.city import City


@pytest.fixture()
def city():
    return City.objects.create(name="São Paulo", state="SP")
