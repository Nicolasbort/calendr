import pytest
from api.models.profile import Profile


@pytest.fixture()
def profile(plan, profession):
    profile = Profile(
        username="username",
        email="username@example.com",
        first_name="First",
        last_name="Last",
        genre="M",
        is_staff=False,
        is_superuser=False,
        plan=plan,
        profession=profession,
    )
    profile.set_password("password")
    profile.save()

    return profile


@pytest.fixture()
def admin_profile(plan, profession):
    profile = Profile(
        username="admin",
        email="admin@example.com",
        first_name="Admin",
        last_name="Auto",
        genre="M",
        is_staff=True,
        is_superuser=True,
        plan=plan,
        profession=profession,
    )
    profile.set_password("password")
    profile.save()

    return profile
