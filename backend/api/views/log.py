import logging

from api.models.patient import Patient
from api.serializers.patient import PatientSerializer
from rest_framework import permissions, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

logger = logging.getLogger("django")


class LogViewSet(viewsets.GenericViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    permission_classes = [permissions.AllowAny]

    @action(methods=["GET"], detail=False, url_path="test-level")
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
