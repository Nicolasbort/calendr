from api.models.notification import Notification
from api.permissions import IsAdminOrProfessional
from api.serializers.notification import (
    NotificationManySerializer,
    NotificationSerializer,
)
from django.utils import timezone
from drf_spectacular.utils import extend_schema
from rest_framework import mixins, status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class NotificationViewSet(
    viewsets.ViewSet, viewsets.GenericViewSet, mixins.ListModelMixin
):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminOrProfessional]

    def get_queryset(self):
        if self.request.user.is_staff:
            return self.queryset

        queryset = self.queryset.filter(profile_to=self.request.user)

        if self.action in ["list", "retrieve"]:
            return queryset

        return queryset.filter(read_at__isnull=True)

    @extend_schema(request=None)
    @action(methods=["POST"], detail=True, url_path="read")
    def read(self, request, **kwargs):
        notification = self.get_object()
        notification.read_at = timezone.now()
        notification.save(update_fields=["read_at"])

        return Response(
            status=status.HTTP_200_OK,
            data=NotificationSerializer(instance=notification).data,
        )

    @extend_schema(request=NotificationManySerializer, responses={204: None})
    @action(methods=["POST"], detail=False, url_path="read-many")
    def read_many(self, request, **kwargs):
        serializer = NotificationManySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.get_queryset().filter(pk__in=serializer.data["ids"]).update(
            read_at=timezone.now()
        )

        return Response(status=status.HTTP_204_NO_CONTENT)
