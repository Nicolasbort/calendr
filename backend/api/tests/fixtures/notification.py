import pytest
from api.constants.notification import TypeChoices
from api.models.notification import Notification


@pytest.fixture()
def notification(profile, patient_profile):
    return Notification.objects.create(
        profile_from=patient_profile,
        profile_to=profile,
        data={
            "message": "Notification message",
            "type": TypeChoices.APPOINTMENT_CREATED,
        },
    )


@pytest.fixture()
def notifications(profile, patient_profile):
    notifications = []

    for i in range(5):
        notifications.append(
            Notification(
                profile_from=patient_profile,
                profile_to=profile,
                data={
                    "message": f"Notification message {i}",
                    "type": TypeChoices.APPOINTMENT_CREATED,
                },
            )
        )

    return Notification.objects.bulk_create(notifications)
