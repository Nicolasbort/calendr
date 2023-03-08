from rest_framework.permissions import BasePermission


class BelongsToProfessional(BasePermission):
    def has_object_permission(self, request, view, obj):
        try:
            return (
                request.user.is_staff or request.user.id == obj.professional.profile.id
            )
        except:
            return False
