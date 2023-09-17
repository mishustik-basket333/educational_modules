from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# class Moderator(AbstractUser):
#     """ Класс для отображения данных о модераторе"""
#     title = models.CharField(max_length=100, verbose_name='название')
#     description = models.TextField(verbose_name='описание', **NULLABLE)
#     # id_user = models.OneToOneField("User", verbose_name="пользователь",
#     #                                related_name="id_user", on_delete=models.SET_NULL, **NULLABLE)
#
#     class Meta:
#         verbose_name = 'модератор'
#         verbose_name_plural = 'модераторы'
#         ordering = ['title']
#
#     def __str__(self):
#         return self.email


#
# class Teacher(AbstractUser):
#     """ Класс для отображения данных о преподавателе"""
#     title = models.CharField(max_length=100, verbose_name='название')
#     description = models.TextField(verbose_name='описание', **NULLABLE)
#
#     class Meta:
#         verbose_name = 'преподаватель'
#         verbose_name_plural = 'преподаватели'
#         ordering = ['title']
#
#     def __str__(self):
#         return self.email


class User(AbstractUser):
    """Класс для отображения пользователей"""

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=235, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=235, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='educational-modules/users/photo', verbose_name='аватар', **NULLABLE)
    # id_moderator = models.OneToOneField(Moderator, verbose_name="модератор",
    #                                     related_name="id_moderator", on_delete=models.SET_NULL, **NULLABLE)
    # id_teacher = models.OneToOneField(Teacher, verbose_name="преподаватель", related_name="id_teacher",
    #                                   on_delete=models.SET_NULL, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
