import pytest
from api.models.patient import Patient


@pytest.fixture()
def patient(professional, patient_profile):
    return Patient.objects.create(
        professional=professional,
        profile=patient_profile,
        notify_pending_payment=True,
        first_name="Prof. First",
        last_name="Prof. Last",
    )


@pytest.fixture()
def other_patient(professional, other_patient_profile):
    return Patient.objects.create(
        professional=professional,
        profile=other_patient_profile,
        notify_pending_payment=True,
        first_name="Prof. Other First",
        last_name="Prof. Other Last",
    )


@pytest.fixture()
def patient_fields():
    return [
        "id",
        "first_name",
        "last_name",
        "full_name",
        "email",
        "phone",
        "professional",
        "is_confirmed",
        "notify_pending_payment",
        "notify_appointment",
        "appointments",
        "created_at",
        "modified_at",
    ]
