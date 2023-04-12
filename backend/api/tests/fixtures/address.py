import pytest
from api.models.address import Address


@pytest.fixture()
def address(city):
    return Address.objects.create(
        city=city,
        street="Street",
        number="123",
        district="District",
        complement="Complement",
    )
