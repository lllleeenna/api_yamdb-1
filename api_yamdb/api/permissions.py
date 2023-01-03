from rest_framework import permissions

ROLE = ('admin', 'moderator')
DANGEROUS_METHOD = ('PUT', 'PUTCH', 'DELETE')


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
