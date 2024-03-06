from rest_framework.permissions import BasePermission


class OnlySuperUserOrStaff(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser and request.user.is_staff)