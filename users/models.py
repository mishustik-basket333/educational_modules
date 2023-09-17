from django.contrib.auth.models import AbstractUser
from django.db import models
from multiselectfield import MultiSelectField

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    """Класс для отображения пользователей"""

    ROLES_CHOICES = (
        ('moderator', 'moderator'),
        ('teacher', 'teacher'),
    )

    username = None

    email = models.EmailField(unique=True, verbose_name='почта')
    phone = models.CharField(max_length=30, verbose_name='телефон', **NULLABLE)
    country = models.CharField(max_length=235, verbose_name='страна', **NULLABLE)
    city = models.CharField(max_length=235, verbose_name='город', **NULLABLE)
    avatar = models.ImageField(upload_to='educational-modules/users/photo', verbose_name='аватар', **NULLABLE)
    roles = MultiSelectField(choices=ROLES_CHOICES, verbose_name='роль пользователя', max_length=23, **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'пользователи'

    def __str__(self):
        return self.email
