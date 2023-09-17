from rest_framework import serializers

from modules.models import Modules


class ModulesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор обучающего модуля """

    count_users = serializers.SerializerMethodField()

    def get_count_users(self, obj):
        return obj.id_users.count()

    class Meta:
        model = Modules
        fields = ("id", "title", "description", "photo", "video", "id_category", "id_users", "count_users",)


class ModulesSmallSerializer(serializers.ModelSerializer):
    """ Класс сериализатор обучающего модуля, сокращенный """

    class Meta:
        model = Modules
        fields = ("id", "title", "description", "photo",)
