from django.conf import settings
from django.db import models

from users.models import User


class Ad(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    author = models.ForeignKey(User, related_name='ads', on_delete=models.CASCADE, verbose_name='Автор')
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    description = models.CharField(max_length=2000, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', blank=True, null=True, verbose_name="Картинка")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        ordering = ['created_at']


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE, verbose_name='Автор')
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, verbose_name='Объявление')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

