from rest_framework import serializers

from modules.serializers import ModulesSmallSerializer
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с полным отображением данных"""

    modules = ModulesSmallSerializer(source='id_users', read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "first_name", "last_name", 'phone', 'country', 'city', "roles",
                  "modules")


class UserPublishedSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с ограниченным отображением данных"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", )
