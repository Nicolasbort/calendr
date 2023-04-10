from rest_framework.permissions import BasePermission


class IsProfessional(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        try:
            return bool(request.user.professional)
        except:
            return False
