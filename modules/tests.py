from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Modules
from users.models import User


class ModulesTestCase(APITestCase):
    """Тест модулей"""

    def setUp(self) -> None:
        """Создание тестовой привычки"""

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="1255753717",
        )

        self.test_user = User.objects.create(
            email='lalala@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="111",

        )

        self.data = Modules.objects.create(
                title="python",
                description="all course",
                id_users=[self.user.pk, self.test_user.pk],
        )

        self.client.force_authenticate(user=self.user)

    def test_1_create_modules(self):
        """ Тестирование создания модуля """

        response = self.client.post('/modules/create/')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)

    # def test_2_list_modules(self):
    #     """ Тестирование вывода списка пользователей """
    #
    #     self.client.force_authenticate(user=self.user)
    #
    #     response = self.client.get('/modules/')
    #
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(User.objects.all().count(), 1)
