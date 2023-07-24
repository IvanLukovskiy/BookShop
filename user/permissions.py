from rest_framework import permissions


class UserListPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)


class UserObjectPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if obj.status == 'Ven':
            return bool(request.user and request.user.is_staff)

        elif obj.status == 'Cus':
            return bool(request.user and (request.user.is_staff or
                                          request.user.status == 'Ven'))


class OrderPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff or
                                      request.user.status == 'Ven'))

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.creator == request.user or request.user.is_staff


class OrderItemsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and (request.user.is_staff or
                                      request.user.status == 'Ven'))

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return bool(request.user and request.user.is_staff)
