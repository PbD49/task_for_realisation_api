from django.db import models


# Create your models here.
class Blog(models.Model):
    user = models.IntegerField(verbose_name='Пользователь')
    title = models.CharField(max_length=100, verbose_name='Имя записи')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')
    is_published = models.BooleanField(default=True, verbose_name='Публикация')

    def __str__(self):
        return self.title
