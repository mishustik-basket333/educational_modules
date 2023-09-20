from django.db import models

from categories.models import Category
from users.models import NULLABLE, User


class Modules(models.Model):
    """Класс для отображения образовательных модулей"""
    title = models.CharField(max_length=100, verbose_name='название образовательного модуля')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    photo = models.ImageField(upload_to='educational-modules/modules/photo', verbose_name='фото', **NULLABLE)
    video = models.FileField(upload_to='educational-modules/modules/video', verbose_name='видео', **NULLABLE)
    id_category = models.ForeignKey(Category, verbose_name="категория", on_delete=models.SET_NULL, **NULLABLE)
    id_users = models.ManyToManyField(User, verbose_name="пользователь", related_name='id_users', **NULLABLE)
    count_views = models.PositiveIntegerField(verbose_name="кол-во просмотров", default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'образовательный модуль'
        verbose_name_plural = 'образовательные модули'
