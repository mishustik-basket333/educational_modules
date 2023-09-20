from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
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
            roles=("moderator", "teacher"),
        )

        # self.test_user = User.objects.create(
        #     email='lalala@example.com',
        #     password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
        #     is_superuser=True,
        #     is_staff=True,
        #     chat_telegram_id="111",
        #
        # )

        self.client.force_authenticate(user=self.user)

        self.data = Category.objects.create(
                title="IT course",
                description="It's good",
        )


    def test_1_create_category(self):
        """ Тестирование создания категории """

        lala = {
            "title": "курсы по физической подготовке",
            "description": "В здоровом теле - здоровй дух",
        }

        response = self.client.post('/categories/create/', data=lala)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)
