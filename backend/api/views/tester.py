import logging

from api.tasks.mailing import send_email
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

logger = logging.getLogger("django")


class TestViewSet(viewsets.GenericViewSet):
    """
    Viewset that define routes for testing purposes
    """

    permission_classes = [permissions.AllowAny]

    @action(methods=["GET"], detail=False, url_path="log-level")
    def test_log_level(self, request, *args, **kwargs):
        level = request.query_params.get("level", None)

        if level is None:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"error": "You must pass a log level via query string"},
            )

        logger = logging.getLogger("django")
        level = level.upper()

        match level:
            case "DEBUG":
                logger.debug("DEBUG message")
            case "INFO":
                logger.info("INFO message")
            case "WARNING":
                logger.warning("WARNING message")
            case "ERROR":
                logger.error("ERROR message")
            case "CRITICAL":
                logger.critical("CRITICAL message")

        return Response(
            status=status.HTTP_200_OK,
            data={"level": level, "message": "Message sent"},
        )

    @action(methods=["GET"], detail=False, url_path="send-email")
    def test_send_email(self, request, *args, **kwargs):
        result = send_email.delay(
            "Test subject",
            "Test body message",
            "bortoluzzinicolas@gmail.com",
            ["nicolas.bortoluzzi@primepass.com"],
        )

        return Response(
            status=status.HTTP_200_OK,
            data={"result": "Email sent"},
        )
