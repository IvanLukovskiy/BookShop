from rest_framework import permissions


class BooksPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return bool(not request.user.is_authenticated or request.user)

        return bool(request.user and (request.user.is_staff or
                                      request.user.status == 'Ven'))

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
