from rest_framework import serializers
from users.models import User


class UsersSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с полным отображением данных"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "first_name", "last_name", 'phone', 'country', 'city',)


class UsersPublishedSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с ограниченным отображением данных"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "first_name", "last_name", )
