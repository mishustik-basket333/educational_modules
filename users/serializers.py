from rest_framework import serializers

from modules.serializers import ModulesSmallSerializer
from users.models import User
from users.validators import TelegramIdValidator, EmailValidator


class UserSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с полным отображением данных"""

    modules = ModulesSmallSerializer(source='id_users', read_only=True, many=True)

    class Meta:
        model = User
        fields = ("id", "email", "chat_telegram_id", "first_name", "first_name", "last_name", 'phone', 'country',
                  'city', "roles", "modules")
        validators = [
            TelegramIdValidator(field='chat_telegram_id'),
            EmailValidator(field="email")
        ]


class UserPublishedSerializer(serializers.ModelSerializer):
    """ Сериализатор пользователя с ограниченным отображением данных"""

    class Meta:
        model = User
        fields = ("id", "email", "first_name", "last_name", )
