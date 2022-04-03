from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCurrentUserOrReadOnly(BasePermission):
    """
    The request of current a user, or is a read-only request
    """
    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or obj == request.user


class IsOptions(BasePermission):
    """
    The request type is OPTIONS
    """
    def has_permission(self, request, view):
        return request.method == 'OPTIONS'
