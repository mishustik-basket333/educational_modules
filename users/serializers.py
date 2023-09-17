from rest_framework import serializers

from modules.serializers import ModulesSerializer
from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с полным отображением данных"""

    modules = ModulesSerializer(source='id_users', read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "first_name", "last_name", 'phone', 'country', 'city', "modules")


class UsersPublishedSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с ограниченным отображением данных"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "first_name", "last_name", )
