from rest_framework import permissions

class IsSuperAdmin(permissions.BasePermission):
    message = "You do not have permission to access this resource."

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        return False