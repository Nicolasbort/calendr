import json

import pytest
from rest_framework.test import APIClient


class CustomAPIClient(APIClient):
    def post(self, path, data=None, content_type="application/json", **kwargs):
        data = json.dumps(data)
        return super().post(path, data=data, content_type=content_type, **kwargs)

    def patch(self, path, data=None, content_type="application/json", **kwargs):
        data = json.dumps(data)
        return super().patch(path, data=data, content_type=content_type, **kwargs)


@pytest.fixture()
def admin_api(admin_profile):
    client = CustomAPIClient()
    client.force_authenticate(admin_profile)

    return client


@pytest.fixture()
def professional_api(profile, professional):
    client = CustomAPIClient()
    client.force_authenticate(profile)

    return client


@pytest.fixture()
def patient_api(patient_profile, patient):
    client = CustomAPIClient()
    client.force_authenticate(patient_profile)

    return client


@pytest.fixture()
def no_auth_api():
    return CustomAPIClient()
