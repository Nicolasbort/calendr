import pytest
from api.constants.appointment import TypeChoices
from api.models.appointment import Appointment


@pytest.fixture()
def appointment(professional, patient, slot):
    return Appointment.objects.create(
        professional=professional,
        patient=patient,
        slot=slot,
        date="2023-01-01",
        time_start="15:00",
        time_end="16:00",
        price=150,
        type=TypeChoices.ONLINE,
    )
