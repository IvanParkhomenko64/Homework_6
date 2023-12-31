# Generated by Django 4.2.2 on 2023-07-09 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 9, 22, 1, 30, 692951), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='slug',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='slug'),
        ),
    ]
