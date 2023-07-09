from django.db import models
import datetime

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name='Заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    body = models.TextField(verbose_name='Cодержимое')
    image = models.ImageField(upload_to='blog/', verbose_name='Превью', **NULLABLE)
    date_of_creation = models.DateTimeField(verbose_name='Дата создания', null=True, default=datetime.datetime.now())
    is_published = models.BooleanField(verbose_name='Опубликовано', default=True)
    views_count = models.IntegerField(default=0, verbose_name='Количество просмотров')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ('title',)
