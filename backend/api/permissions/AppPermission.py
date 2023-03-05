from rest_framework.permissions import BasePermission


class AppPermission(BasePermission):
    def has_permission(self, request, view):
        is_admin = bool(request.user and request.user.is_staff)

        if is_admin:
            return True

        return super().has_permission(request, view)

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
