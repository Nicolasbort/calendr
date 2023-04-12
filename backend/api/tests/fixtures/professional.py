import pytest
from api.models.professional import Professional


@pytest.fixture()
def professional(profile, profession, plan, address):
    return Professional.objects.create(
        genre="M", profession=profession, plan=plan, profile=profile, address=address
    )


@pytest.fixture()
def other_professional(other_profile, other_profession, premium_plan):
    return Professional.objects.create(
        genre="F", profession=other_profession, plan=premium_plan, profile=other_profile
    )


@pytest.fixture()
def admin_professional(admin_profile, profession, plan):
    return Professional.objects.create(
        genre="M", profession=profession, plan=plan, profile=admin_profile
    )
