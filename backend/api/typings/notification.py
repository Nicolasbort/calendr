from typing import TypedDict

from api.constants.notification import TypeChoices


class NotificationData(TypedDict):
    message: str
    type: TypeChoices
