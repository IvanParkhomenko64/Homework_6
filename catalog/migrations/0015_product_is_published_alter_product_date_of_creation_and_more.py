# Generated by Django 4.2.2 on 2023-07-23 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0014_product_owner_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_published',
            field=models.BooleanField(default=False, verbose_name='Опубликовано'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 13, 18, 31, 385089), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 23, 13, 18, 31, 385089), null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
