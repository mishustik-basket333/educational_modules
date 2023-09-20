from rest_framework import status
from rest_framework.test import APITestCase

from modules.models import Modules
from users.models import User


class ModulesTestCase(APITestCase):
    """Тест модулей"""

    def setUp(self) -> None:
        """Создание тестовой """

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="1255753717",
            roles=("moderator", "teacher"),
        )

        self.data = Modules.objects.create(
                title="python",
                description="all course",
        )

        self.client.force_authenticate(user=self.user)

    def test_1_create_modules(self):
        """ Тестирование создания модуля """

        data = {
            "title": "test",
            "description": "test",
            "id_users": self.user.id
        }

        response = self.client.post('/modules/create/', data=data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)

    def test_2_list_modules(self):
        """ Тестирование вывода списка модулей """

        response = self.client.get('/modules/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Modules.objects.all().count(), 1)

    def test_3_list_all_modules(self):
        """ Тестирование вывода полных данных списка модулей """

        response = self.client.get('/modules/all/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Modules.objects.all().count(), 1)

    def test_4_update_modules(self):
        """ Тестирование обновления данных о modules """

        data = {
                "title": "test",
        }

        response = self.client.put(f'/modules/update/{self.data.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], 'test')

    def test_5_destroy_modules(self):
        """ Тестирование удаления modules """

        response = self.client.delete(f'/modules/delete/{self.data.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Modules.objects.all().exists())
        self.assertEqual(Modules.objects.all().count(), 0)
