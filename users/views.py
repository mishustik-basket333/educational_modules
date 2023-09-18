from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import User
from users.pagination import UserPagination
from users.permissions import IsModeratorPermission, IsTeacherPermission
from users.serializers import UserSerializer, UserPublishedSerializer
from users.services import welcome_send_telegram, welcome_send_mail


class UsersCreateAPIView(generics.CreateAPIView):
    """ Создание пользователя"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        # print("test")
        # print(request.data["chat_telegram_id"])
        # welcome_send_mail(email=request.data["email"])
        # welcome_send_telegram(chat_telegram_id="@ii_ildar")
        # welcome_send_mail("iiiskhakov1990@gmail.com")
        # welcome_send_telegram(chat_telegram_id="@ii_ildar")
        return self.create(request, *args, **kwargs)

    # def get_queryset(self):
    #     print(self.chat_telegram_id)
    #     # if self.chat_telegram_id:
    #     #     welcome_send_telegram(self.chat_telegram_id)
    #     return User.objects.all()


class UserPublishedListAPIView(generics.ListAPIView):
    """ Вывод списка пользователей для авторизованны пользователей с ограниченными данными"""

    serializer_class = UserPublishedSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()


class UserListAPIView(generics.ListAPIView):
    """ Вывод списка расширенных данных пользователей """

    serializer_class = UserSerializer
    pagination_class = UserPagination
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return User.objects.all()


class UsersRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод данных одного пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if "moderator" in self.request.user.roles:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.pk)


class UsersUpdateAPIView(generics.UpdateAPIView):
    """ Обновление данных пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if "moderator" in self.request.user.roles:
            return User.objects.all()
        return User.objects.filter(id=self.request.user.pk)


class UsersDestroyAPIView(generics.DestroyAPIView):
    """ Удаление данных пользователя"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated & IsModeratorPermission]

    def get_queryset(self):
        return User.objects.all()
