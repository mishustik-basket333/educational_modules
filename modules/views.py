from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from modules.models import Modules
from modules.pagination import ModulesPagination
from modules.serializers import ModulesSerializer, ModulesSmallSerializer
from users.permissions import IsModeratorPermission, IsTeacherPermission


class ModulesCreateAPIView(generics.CreateAPIView):
    """ Создание обучающего модуля """

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def perform_create(self, serializer):
        data_modules = serializer.save()
        data_modules.user = self.request.user
        data_modules.save()


class ModulesPublishedListAPIView(generics.ListAPIView):
    """ Вывод списка обучающих модулей для авторизованных пользователей с ограниченными данными"""

    serializer_class = ModulesSmallSerializer
    pagination_class = ModulesPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Modules.objects.all()


class ModulesListAPIView(generics.ListAPIView):
    """ Вывод списка расширенных данных обучающих модулей """

    serializer_class = ModulesSerializer
    pagination_class = ModulesPagination
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Modules.objects.all()


class ModulesRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного обучающего модуля"""

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        if "moderator" in self.request.user.roles:
            return Modules.objects.all()
        return Modules.objects.filter(id_users=self.request.user)

    def get_object(self):
        data = super().get_object()
        data.count_views += 1
        data.save()
        return data


class ModulesUpdateAPIView(generics.UpdateAPIView):
    """ Обновление обучающего модуля"""

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated & (IsModeratorPermission | IsTeacherPermission)]

    def get_queryset(self):
        return Modules.objects.all()


class ModulesDestroyAPIView(generics.DestroyAPIView):
    """ Удаление обучающего модуля"""

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated & IsModeratorPermission]

    def get_queryset(self):
        return Modules.objects.all()
