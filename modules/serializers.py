from rest_framework import serializers

from modules.models import Modules
# from modules.validators import double_reward_validator

class ModulesSerializer(serializers.ModelSerializer):
    """ Класс сериализатор привычки """

    class Meta:
        model = Modules
        fields = '__all__'
        # validators = [
        #     double_reward_validator,
        # ]
