from rest_framework import permissions


class AuthorOrReadOnly(permissions.BasePermission):
    """
    Разрешение на чтение объектов и получение списка объектов.
    Редактирование, удаление возможно только автором.
    Создание возможно аутентифицированным пользователем.
    """

    def has_permission(self, request, view):
        return (
            request.method in permissions.SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
