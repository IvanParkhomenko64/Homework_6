from django.core.management import BaseCommand
import json

from catalog.models import Category, Product


class Command(BaseCommand):

    def handle(self, *args, **options):
        # with open('.\data.json', 'r') as f:
        #     data_list = json.load(f)
        # print(data_list)
        category_list = [
            {'name': 'Фрукты', 'description': 'Фрукты - это Фрукты'},
            {'name': 'Овощи', 'description': 'Овощи - это Овощи'},
            {'name': 'Ягоды', 'description': 'Ягоды - это Ягоды'},
            {'name': 'Мясо', 'description': 'Мясо - это Мясо'},
            {'name': 'Хлеб', 'description': 'Хлеб - это Хлеб'}
        ]

        # for category_item in category_list:
        #     Category.objects.create(**category_item)
        Product.objects.all().delete()
        Category.objects.all().delete()
        category_for_create = []
        for category_item in category_list:
            category_for_create.append(Category(**category_item))

        Category.objects.bulk_create(category_for_create)
