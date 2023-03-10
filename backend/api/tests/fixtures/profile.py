import pytest
from api.models.profile import Profile


@pytest.fixture()
def profile():
    profile = Profile(
        email="username@example.com",
        username="profile",
        first_name="First",
        last_name="Last",
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
        username="other",
        first_name="Other",
        last_name="Last",
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
        username="patient",
        first_name="Patient",
        last_name="Lastname",
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
        username="admin",
        first_name="Admin",
        last_name="Auto",
        is_staff=True,
        is_superuser=True,
    )
    profile.set_password("password")
    profile.save()

    return profile
