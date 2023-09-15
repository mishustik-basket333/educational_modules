from rest_framework import serializers

from modules.models import Modules
from users.serializers import UsersSerializer


# from modules.validators import double_reward_validator

class ModulesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор обучающего модуля """

    # user = UsersSerializer(read_only=True, )

    class Meta:
        model = Modules
        fields = ("id", "title", "description", "photo", "video", "id_category", "id_users")
