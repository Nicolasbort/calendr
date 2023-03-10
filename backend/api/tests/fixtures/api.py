import pytest
from rest_framework.test import APIClient


@pytest.fixture()
def admin_api(admin_profile):
    client = APIClient()
    client.force_authenticate(admin_profile)

    return client


@pytest.fixture()
def professional_api(profile):
    client = APIClient()
    client.force_authenticate(profile)

    return client


@pytest.fixture()
def patient_api(patient_profile):
    client = APIClient()
    client.force_authenticate(patient_profile)

    return client
