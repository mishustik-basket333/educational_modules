from django.db import models

from categories.models import Category
from users.models import NULLABLE, User


class Modules(models.Model):
    """Класс для отображения образовательных модулей"""
    title = models.CharField(max_length=100, verbose_name='название образовательного модуля')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    photo = models.ImageField(upload_to='educational-modules/', verbose_name='фото', **NULLABLE)
    video = models.FileField(upload_to='video-files/', verbose_name='видео', **NULLABLE)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, **NULLABLE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'образовательный модуль'
        verbose_name_plural = 'образовательные модули'
