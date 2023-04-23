import pytest
from api.models.profile import Profile


@pytest.fixture()
def profile():
    return Profile.objects.create(
        email="username@example.com",
        first_name="Profile",
        last_name="Lastname",
        is_staff=False,
        is_superuser=False,
    )


@pytest.fixture()
def other_profile():
    return Profile.objects.create(
        email="other@example.com",
        first_name="Other",
        last_name="Last",
        is_staff=False,
        is_superuser=False,
    )


@pytest.fixture()
def patient_profile():
    return Profile.objects.create(
        email="patient@example.com",
        first_name="Patient",
        last_name="Lastname",
        is_staff=False,
        is_superuser=False,
    )


@pytest.fixture()
def other_patient_profile():
    return Profile.objects.create(
        email="otherpatient@example.com",
        first_name="Other Patient",
        last_name="Lastname",
        is_staff=False,
        is_superuser=False,
    )


@pytest.fixture()
def admin_profile():
    return Profile.objects.create(
        email="admin@example.com",
        first_name="Admin",
        last_name="Auto",
        is_staff=True,
        is_superuser=True,
    )
