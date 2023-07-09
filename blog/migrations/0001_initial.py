# Generated by Django 4.2.2 on 2023-07-09 12:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('slug', models.CharField(max_length=150, verbose_name='slug')),
                ('body', models.TextField(verbose_name='Cодержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blog/', verbose_name='Превью')),
                ('date_of_creation', models.DateTimeField(default=datetime.datetime(2023, 7, 9, 16, 46, 42, 149474), null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
                'ordering': ('title',),
            },
        ),
    ]
