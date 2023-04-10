import logging

from api.constants.third_party import ThirdPartyNameChoices
from api.models.appointment import Appointment
from api.models.third_party import ThirdParty
from api.services.third_parties.google_calendar import GoogleCalendar
from calendr.celery import celery_app

logger = logging.getLogger("django")


@celery_app.task(name="schedule_event")
def schedule_event(
    professional_id: str, appointment_id: str, patient_emails: list[str]
):
    logger.info(
        f"""Schedule Event: Starting event schedule.
        Professional ID: {professional_id}
        Appointment ID: {appointment_id}
        Patients: {patient_emails}"""
    )

    third_party_calendar = ThirdParty.get_professional_third_party_by_name(
        professional_id, ThirdPartyNameChoices.GOOGLE_CALENDAR
    )

    if not third_party_calendar:
        logger.info(
            f"Schedule Event: Professional {professional_id} doesn't have a Google Calendar integration"
        )
        return

    appointment: Appointment = Appointment.objects.get(pk=appointment_id)

    google_calendar = GoogleCalendar(third_party_calendar.access_token)
    success, event = google_calendar.create_event(
        appointment.time_start, appointment.time_end, "", "", patient_emails
    )

    if not success:
        logger.error(
            f"Schedule Event: Failed to schedule an event. Appointment ID: {appointment_id}. Error: {event}"
        )
        return

    appointment.link = event.get("htmlLink")
    appointment.save(update_fields=["link"])

    logger.info(
        f"Schedule Event: Event scheduled successfully. Appointment ID: {appointment_id}, Link: {appointment.link}"
    )
