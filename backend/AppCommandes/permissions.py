from rest_framework import permissions


class IsSuperOrOnlyGet(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_superuser or (
            request.method == "GET" and request.user.is_authenticated
        ):
            return True
        return False


class OnlyGet(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method == "GET"


class IsSuper(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
