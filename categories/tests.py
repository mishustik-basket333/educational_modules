from rest_framework import status
from rest_framework.test import APITestCase

from categories.models import Category
from users.models import User


class CategoriesTestCase(APITestCase):
    """Тест модулей"""

    def setUp(self) -> None:
        """Создание тестовых данных"""

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            chat_telegram_id="1255753717",
            roles=("moderator", "teacher"),
        )

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
        self.assertEqual(Category.objects.all().count(), 2)

    def test_2_list_category(self):
        """ Тестирование вывода списка категорий """

        data = {
                "title": "IT course",
                "description": "It's good"
        }

        response = self.client.get('/categories/', data=data)

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Category.objects.all().count(), 1)

    def test_3_retrieve_categories(self):
        """ Тестирование вывода одного пользователя """

        response = self.client.get(f'/categories/{self.data.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 1)

    def test_4_update_categories(self):
        """ Тестирование обновления данных о category """

        data = {
                "title": "test",
                "description": "It's good"
        }

        response = self.client.put(f'/categories/update/{self.data.pk}/', data=data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["title"], 'test')

    def test_5_destroy_category(self):
        """ Тестирование удаления category """

        response = self.client.delete(f'/categories/delete/{self.data.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.all().exists())
        self.assertEqual(Category.objects.all().count(), 0)
