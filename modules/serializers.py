from rest_framework import serializers

from modules.models import Modules
from users.models import User


class ModulesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор обучающего модуля """

    # users = UserSerializer(source='id_users', read_only=True, many=True)

    count_users = serializers.SerializerMethodField()
    list_u = serializers.SerializerMethodField()

    def get_count_users(self, obj):
        return obj.id_users.count()

    def get_list_u(self, obj):
        return str([f"{u.email, u.city}" for u in obj.id_users.all()])

    class Meta:
        model = Modules
        fields = ("id", "title", "description", "photo", "video", "id_category", "id_users", "count_users", "list_u",)


class ModulesSmallSerializer(serializers.ModelSerializer):
    """ Класс сериализатор обучающего модуля, сокращенный """

    class Meta:
        model = Modules
        fields = ("id", "title", "description", "photo",)
