from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    last_name = models.CharField(max_length=100, verbose_name='Имя')
    first_name = models.CharField(max_length=100, verbose_name='Фамилия')
    # username =

    def __str__(self):
        return self.last_name


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100, verbose_name='Имя записи')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
