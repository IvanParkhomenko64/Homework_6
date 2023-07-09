# Generated by Django 4.2.2 on 2023-06-25 10:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_contacts_alter_product_date_of_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='message',
            field=models.TextField(blank=True, null=True, verbose_name='Сообщение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='date_of_creation',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 14, 21, 53, 761772), null=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='product',
            name='last_modified_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 6, 25, 14, 21, 53, 761772), null=True, verbose_name='Дата последнего изменения'),
        ),
    ]