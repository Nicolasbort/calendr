import pytest
from api.models.patient import Patient


@pytest.fixture()
def patient(professional, patient_profile):
    return Patient.objects.create(
        professional=professional, profile=patient_profile, notify_pending_payment=True
    )


@pytest.fixture()
def admin_patient(admin_professional, patient_profile):
    return Patient.objects.create(
        professional=admin_professional,
        profile=patient_profile,
        notify_pending_payment=True,
    )


@pytest.fixture()
def patient_fields():
    return [
        "id",
        "first_name",
        "last_name",
        "email",
        "username",
        "phone",
        "profile",
        "professional",
        "notify_pending_payment",
        "created_at",
        "modified_at",
    ]
