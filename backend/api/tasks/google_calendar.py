import logging

from api.constants.third_party import ThirdPartyNameChoices
from api.models.appointment import Appointment
from api.models.patient import Patient
from api.models.third_party import ThirdParty
from api.services.third_parties.google_calendar import GoogleCalendar
from calendr.celery import celery_app

logger = logging.getLogger("django")


@celery_app.task(name="schedule_event")
def schedule_event(professional_id: str, appointment_id: str, patient_ids: list[str]):
    logger.info(
        f"""Schedule Event: Starting event schedule.
        Professional ID: {professional_id}
        Appointment ID: {appointment_id}
        Patients: {patient_ids}"""
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
    professional = appointment.professional
    patients: list[Patient] = Patient.objects.filter(pk__in=patient_ids).all()
    event_title = f"Consulta com {professional.profile.first_name}"

    google_calendar = GoogleCalendar(third_party_calendar.access_token)
    success, event = google_calendar.create_event(
        appointment, event_title, "", patients
    )

    if not success:
        logger.error(
            f"Schedule Event: Failed to schedule an event. Appointment ID: {appointment_id}. Error: {event}"
        )
        return

    appointment.link = event["htmlLink"]
    appointment.save(update_fields=["link"])

    logger.info(
        f"Schedule Event: Event scheduled successfully. Appointment ID: {appointment_id}, Link: {appointment.link}"
    )
