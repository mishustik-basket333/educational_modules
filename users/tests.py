from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """ Тестирование пользователя"""

    def setUp(self) -> None:
        """ Создание тестовых данных"""
        self.data = {
            "email": "test@lalala.ru",
            "is_active": "True",
            "is_superuser": "True",
            "roles": ("moderator", 'teacher'),
            "password": "pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=",
            "chat_telegram_id": "111",
            "first_name": "Ivan"
        }

    def test_1_create_user(self):
        """ Тестирование создания юзера """

        response = self.client.post('/users/create/', data=self.data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.all().count(), 1)

    def test_2_list_user(self):
        """ Тестирование вывода списка пользователей """
        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            chat_telegram_id="111",
            roles=("moderator", "teacher")
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get('/users/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 1)

    def test_3_list_user(self):
        """ Тестирование вывода полного списка пользователей """

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            chat_telegram_id="111",
            roles=("moderator", "teacher")
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get('/users/all/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 1)

    def test_4_retrieve_user(self):
        """ Тестирование вывода одного пользователя """

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            chat_telegram_id="111",
            roles=("moderator", "teacher")
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.get(f'/users/{self.user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.all().count(), 1)

    def test_5_update_user(self):
        """ Тестирование обновления данных о пользователе """

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            chat_telegram_id="111",
            roles=("moderator", "teacher")
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.put(f'/users/update/{self.user.pk}/', data=self.data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["first_name"], 'Ivan')

    def test_6_destroy_user(self):
        """ Тестирование удаления пользователя """

        self.user = User.objects.create(
            email='test@example.com',
            password='pbkdf2_sha256$600000$mZl73sbkndeVLzzLCcMCwb$eKIy2Pik7IhuL5Lt8MOX+QGP1jYPpn+6IRNVrWPmiO8=',
            is_superuser=True,
            is_staff=True,
            is_active=True,
            chat_telegram_id="111",
            roles=("moderator", "teacher")
        )

        self.client.force_authenticate(user=self.user)

        response = self.client.delete(f'/users/delete/{self.user.pk}/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(User.objects.all().exists())
        self.assertEqual(User.objects.all().count(), 0)
