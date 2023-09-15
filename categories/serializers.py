from rest_framework import serializers

from categories.models import Category



# from modules.validators import double_reward_validator

class CategoriesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор категорий """

    # user = UsersSerializer(read_only=True, )

    class Meta:
        model = Category
        fields = ("id", "title", "description", "photo",)
