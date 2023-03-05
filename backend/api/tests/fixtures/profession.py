import pytest
from api.models.profession import Profession


@pytest.fixture()
def profession():
    return Profession.objects.create(name="Psico")


@pytest.fixture()
def other_profession():
    return Profession.objects.create(name="Other Psico")
