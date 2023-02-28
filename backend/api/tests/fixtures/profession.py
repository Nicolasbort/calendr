import pytest
from api.models.profession import Profession


@pytest.fixture()
def profession():
    return Profession.objects.create(name="Admin")
