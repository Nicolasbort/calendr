import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCustomerProfessionalViewSet:
    @staticmethod
    def test_get_default_professional_calendar(patient_api, calendar, slot, other_slot):
        other_slot.week_day = 2
        other_slot.save(update_fields=["week_day"])

        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"username": calendar.professional.profile.username},
        )

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert str(calendar.id) == returned_calendar["id"]
        assert str(calendar.professional.id) == returned_calendar["professional"]["id"]
        assert calendar.name == returned_calendar["name"]
        assert returned_calendar["is_default"] == True
        assert returned_calendar["is_active"] == True
        assert len(returned_calendar["periods"]) == 2

    @staticmethod
    def test_get_calendar_not_active(patient_api, calendar_not_active):
        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"username": calendar_not_active.professional.profile.username},
        )

        response = patient_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_not_default(patient_api, calendar_not_default):
        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"username": calendar_not_default.professional.profile.username},
        )

        response = patient_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_not_active_and_default(
        patient_api, calendar_not_active_and_default
    ):
        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={
                "username": calendar_not_active_and_default.professional.profile.username
            },
        )

        response = patient_api.get(url)

        assert response.status_code == 404
