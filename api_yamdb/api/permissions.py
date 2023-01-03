from rest_framework import permissions


class IsAdminOrSuperuserOrReadOnly(permissions.BasePermission):
    """Разрешение, позволяющее редактировать объект только
    админитратору.
    """

    def has_permission(self, request, view):
        return (
            permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.is_admin or request.user.is_superuser
                )
            )
        )

    def has_object_permission(self, request, view, obj):
        return (
            permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.is_admin or request.user.is_superuser
                )
            )
        )
