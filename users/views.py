from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.pagination import UserPagination
from users.serializers.user import UserSerializer, UserPublishedSerializer


class UsersCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserPublishedListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей для авторизованны пользователей с ограниченными данными"""

    serializer_class = UserPublishedSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return User.objects.filter(user=self.request.user)
        return User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """ Полный вывод списка пользователей"""

    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return User.objects.filter(user=self.request.user)
        return User.objects.all()


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод данных одного пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.pk)
        # return User.objects.all()


class UsersUpdateAPIView(generics.UpdateAPIView):
    """ Обновление данных пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.pk)
        # return User.objects.all()


class UsersDestroyAPIView(generics.DestroyAPIView):
    """ Удаление данных пользователя"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()
