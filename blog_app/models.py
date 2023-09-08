from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True,
                            db_index=True, verbose_name='URL')
    content = models.TextField(blank=True, verbose_name='Текст статьи')
    photo = models.ImageField(
        upload_to='photos/%Y/%m/%d/', verbose_name='Изображение')
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name='Дата изменения')
    user = models.ForeignKey(
        'User', on_delete=models.PROTECT, verbose_name='Пользователь')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ['time_create', 'title']


class User(AbstractUser):
    slug = models.SlugField(max_length=255,
                            verbose_name='URL')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('user', kwargs={'user_slug': self.slug})
