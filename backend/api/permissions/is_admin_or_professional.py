from rest_framework.permissions import BasePermission


class IsAdminOrProfessional(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff:
            return True

        try:
            return bool(request.user.professional)
        except:
            return False
