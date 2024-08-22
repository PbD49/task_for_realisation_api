from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser


def get_permissions(self):
    """Метод для определения прав доступа
       удалять и изменять данные может только
       админитратор или авторизованный пользователь
    """
    if self.request.method in ['PUT', 'DELETE']:
        return [IsAdminUser()]
    return [IsAuthenticatedOrReadOnly()]