from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

from modules.models import Modules
from modules.pagination import ModulesPagination
from modules.serializers import ModulesSerializer


class ModulesCreateAPIView(generics.CreateAPIView):
    """ Создание обучающего модуля """

    serializer_class = ModulesSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        data_modules = serializer.save()
        data_modules.user = self.request.user
        data_modules.save()


class ModulesListAPIView(generics.ListAPIView):
    """ Вывод списка обучающих модулей, принадлежащих пользователю """

    serializer_class = ModulesSerializer
    pagination_class = ModulesPagination
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Modules.objects.filter(id_users=self.request.user)
        return Modules.objects.all()


class ModulesRetrieveAPIView(generics.RetrieveAPIView):
    """ Вывод одного обучающего модуля"""

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Modules.objects.filter(id_users=self.request.user)
        # return Modules.objects.all()


class ModulesUpdateAPIView(generics.UpdateAPIView):
    """ Обновление обучающего модуля"""

    serializer_class = ModulesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Modules.objects.filter(id_users=self.request.user)
        return Modules.objects.all()


class ModulesDestroyAPIView(generics.DestroyAPIView):
    """ Удаление обучающего модуля"""
    serializer_class = ModulesSerializer
    # permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # return Modules.objects.filter(id_users=self.request.user)
        return Modules.objects.all()
