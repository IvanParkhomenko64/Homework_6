# Generated by Django 4.2.2 on 2023-07-23 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_alter_blog_date_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 13, 18, 31, 385089), null=True, verbose_name='Дата создания'),
        ),
    ]