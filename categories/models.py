from django.db import models

from users.models import NULLABLE


class Category(models.Model):
    title = models.CharField(max_length=30, verbose_name='название')
    description = models.TextField(verbose_name='описание', **NULLABLE)
    photo = models.ImageField(upload_to='educational-modules/categories/photo', verbose_name='фото', **NULLABLE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
