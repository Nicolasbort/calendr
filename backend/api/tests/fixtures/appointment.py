import pytest
from api.constants.appointment import TypeChoices
from api.models.appointment import Appointment


@pytest.fixture()
def appointment(patient, session):
    return Appointment.objects.create(
        patient=patient,
        session=session,
        date="2023-01-01",
        type=TypeChoices.ONLINE,
    )
