import logging

from api.constants.notification import TypeChoices
from api.models.notification import Notification
from api.typings.notification import NotificationData
from calendr.celery import celery_app

logger = logging.getLogger("django")


@celery_app.task(name="create_notification")
def create_notification(
    profile_to_id: str, profile_from_id: str, message: str, type: TypeChoices
):
    data: NotificationData = {"message": message, "type": type}

    notification = Notification.objects.create(
        profile_to=profile_to_id, profile_from=profile_from_id, data=data
    )

    logger.info(f"Create Notification: Notification '{str(notification.id)}' created")
