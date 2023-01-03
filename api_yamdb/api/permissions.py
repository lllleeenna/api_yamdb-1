from rest_framework import permissions


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее редактировать объект администраторам и
    смотреть всем.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'admin'
                or request.user.is_superuser)


class IsAdmin(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее все действия Администраторам
     при любых запросах.
    """
    def has_permission(self, request, view):
        return (request.user.role == 'admin'
                or request.user.is_superuser)


class IsModeratorOrAdmin(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее редактировать объект администраторам и
    смотреть всем.
    """
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'moderator'
                or request.user.role == 'admin'
                or request.user.is_superuser)


class IsAuthor(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее редактировать объект только владельцам.
    """
    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.role == 'moderator'
                or request.user.role == 'admin'
                or request.user.is_superuser
                or obj.author == request.user)
