import pytest
from api.models.professional import Professional


@pytest.fixture()
def professional(profile, profession, plan, address):
    return Professional.objects.create(
        genre="M",
        profession=profession,
        plan=plan,
        profile=profile,
        address=address,
        username="professional",
    )


@pytest.fixture()
def other_professional(other_profile, other_profession, premium_plan):
    return Professional.objects.create(
        genre="F",
        profession=other_profession,
        plan=premium_plan,
        profile=other_profile,
        username="otherprofessional",
    )


@pytest.fixture()
def customer_professional_fields():
    return [
        "id",
        "first_name",
        "last_name",
        "email",
        "phone",
        "username",
        "full_name",
        "address",
        "profession",
        "picture",
        "genre",
        "birthday",
        "bio",
        "registration_number",
    ]
