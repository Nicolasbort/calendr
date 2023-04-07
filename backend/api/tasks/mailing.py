import json
import logging

from api.models.profile import Profile
from calendr.celery import celery_app
from calendr.settings import EMAIL_FROM, SEND_EMAIL_ACTIVE
from django.core.mail import send_mail

logger = logging.getLogger("django")


@celery_app.task(name="send_email")
def send_email(subject: str, message: str, from_email: str, recipient_list: list[str]):
    if not SEND_EMAIL_ACTIVE:
        serialized_data = __get_serialized_data(
            subject, message, from_email, recipient_list
        )

        logger.info(
            f"""SEND_EMAIL_ACTIVE env is empty or false.
            Emails will only be sent when this flag is true.
            Serialized email data: {serialized_data}"""
        )
        return

    success = send_mail(
        subject, message, from_email, recipient_list, fail_silently=False
    )

    if not success:
        serialized_data = __get_serialized_data(
            subject, message, from_email, recipient_list
        )

        logger.warning(
            f"""Error when trying to send email.
            Serialized email data: {serialized_data}"""
        )
        return

    logger.info("Email sent")


@celery_app.task(name="send_activation_email")
def send_activation_email(profile_id):
    profile: Profile = Profile.objects.get(pk=profile_id)

    token = profile.generate_token()

    activation_data = {"token": token}

    if not SEND_EMAIL_ACTIVE:
        serialized_data = json.dumps(activation_data)

        logger.info(
            f"""SEND_EMAIL_ACTIVE env is empty or false.
            Emails will only be sent when this flag is true.
            Serialized email data: {serialized_data}"""
        )
        return

    serialized_data = json.dumps(activation_data)
    success = send_mail(
        "Ative seu email",
        serialized_data,
        EMAIL_FROM,
        [profile.email],
        fail_silently=False,
    )

    if not success:
        serialized_data = json.dumps(activation_data)

        logger.warning(
            f"""Error when trying to send email.
            Serialized email data: {serialized_data}"""
        )
        return

    logger.info("Actication email sent")


def __get_serialized_data(
    subject: str, message: str, from_email: str, recipient_list: list[str]
) -> str:
    data = {
        "subject": subject,
        "message": message,
        "from_email": from_email,
        "recipient_list": recipient_list,
    }

    return json.dumps(data)
