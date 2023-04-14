import pytest
from api.models.profile import Profile


@pytest.fixture()
def profile():
    profile = Profile(
        email="username@example.com",
        first_name="Profile",
        last_name="Lastname",
        username="profilelastname",
        is_staff=False,
        is_superuser=False,
    )
    profile.set_password("password")
    profile.save()

    return profile


@pytest.fixture()
def other_profile():
    profile = Profile(
        email="other@example.com",
        first_name="Other",
        last_name="Last",
        username="otherlast",
        is_staff=False,
        is_superuser=False,
    )
    profile.set_password("password")
    profile.save()

    return profile


@pytest.fixture()
def patient_profile():
    profile = Profile(
        email="patient@example.com",
        first_name="Patient",
        last_name="Lastname",
        username="patientlastname",
        is_staff=False,
        is_superuser=False,
    )
    profile.set_password("password")
    profile.save()

    return profile


@pytest.fixture()
def admin_profile():
    profile = Profile(
        email="admin@example.com",
        first_name="Admin",
        last_name="Auto",
        username="adminauto",
        is_staff=True,
        is_superuser=True,
    )
    profile.create_username()
    profile.set_password("password")
    profile.save()

    return profile
