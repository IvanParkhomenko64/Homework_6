# Generated by Django 4.2.2 on 2023-06-24 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 19, 57, 4, 128410), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 24, 19, 57, 4, 128410), null=True, verbose_name='Дата последнего изменения'),
        ),
    ]
