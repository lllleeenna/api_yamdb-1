from rest_framework import permissions

ROLE = ('admin', 'moderator')
DANGEROUS_METHOD = ('PUT', 'PATCH', 'DELETE')


class ReviewCommentPermission(permissions.BasePermission):
    """Разрешения для отзывов и комментариев.
    смотрят - все
    новый отзыв/коммент - аутентифицированный пользователь
    просмотр по id отзыва/коммента - все
    обновление - автор, модератор, администратор
    удаление - автор, модератор, администратор
    """

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
            or (
                request.user.role in ROLE
                and request.method in DANGEROUS_METHOD
            )
        )

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )


class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее редактировать объект администраторам и
    смотреть всем.
    """
    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or (
                request.user.is_authenticated
                and (
                    request.user.role == 'admin'
                    or request.user.is_superuser
                )
            )
        )


class IsAdmin(permissions.BasePermission):
    """
    Пользовательское разрешение,
    позволяющее все действия Администраторам
     при любых запросах.
    """
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and (
                request.user.role == 'admin'
                or request.user.is_superuser
            )
        )


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
                or request.user.role == ' moderator'
                or request.user.role == 'admin'
                or request.user.is_superuser
                or obj.author == request.user)

    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated)
