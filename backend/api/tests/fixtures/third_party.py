import datetime

import pytest
from api.constants.third_party import ThirdPartyNameChoices
from api.models.third_party import ThirdParty


@pytest.fixture()
def google_third_party(professional):
    return ThirdParty.objects.create(
        name=ThirdPartyNameChoices.GOOGLE_CALENDAR,
        professional=professional,
        access_token="access_token",
        refresh_token="refresh_token",
        expire_at=datetime.datetime.now(),
        scopes=["profile"],
    )
