import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestCustomerProfessionalViewSet:
    @staticmethod
    def test_get_professional_by_username(
        patient_api, professional, customer_professional_fields
    ):
        url = reverse(
            "api:customer-professional-detail",
            kwargs={"multiple_lookup_field": professional.username},
        )

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert set(response.json().keys()) == set(customer_professional_fields)
        assert str(professional.id) == returned_calendar["id"]

    @staticmethod
    def test_get_default_professional_calendar_by_username(
        patient_api, calendar, session, other_session, customer_calendar_fields
    ):
        other_session.week_day = 2
        other_session.save(update_fields=["week_day"])

        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"multiple_lookup_field": calendar.professional.username},
        )

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert set(response.json().keys()) == set(customer_calendar_fields)
        assert str(calendar.id) == returned_calendar["id"]
        assert str(calendar.professional.id) == returned_calendar["professional"]["id"]
        assert calendar.name == returned_calendar["name"]
        assert len(returned_calendar["sessions"]) == 2

    @staticmethod
    def test_get_default_professional_calendar_by_id(
        patient_api, calendar, session, other_session
    ):
        other_session.week_day = 2
        other_session.save(update_fields=["week_day"])

        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"multiple_lookup_field": calendar.professional.id},
        )

        response = patient_api.get(url)

        assert response.status_code == 200

        returned_calendar = response.json()

        assert str(calendar.id) == returned_calendar["id"]
        assert str(calendar.professional.id) == returned_calendar["professional"]["id"]
        assert calendar.name == returned_calendar["name"]
        assert len(returned_calendar["sessions"]) == 2

        assert "is_default" not in returned_calendar
        assert "is_active" not in returned_calendar
        assert "created_at" not in returned_calendar
        assert "modified_at" not in returned_calendar
        assert "deleted_at" not in returned_calendar

    @staticmethod
    def test_get_calendar_not_active(patient_api, calendar_not_active):
        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"multiple_lookup_field": calendar_not_active.professional.id},
        )

        response = patient_api.get(url)

        assert response.status_code == 404

    @staticmethod
    def test_get_calendar_not_default(patient_api, calendar_not_default):
        url = reverse(
            "api:customer-professional-get-calendar-default",
            kwargs={"multiple_lookup_field": calendar_not_default.professional.id},
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
                "multiple_lookup_field": calendar_not_active_and_default.professional.id
            },
        )

        response = patient_api.get(url)

        assert response.status_code == 404
