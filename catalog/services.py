from django.core.cache import cache

from catalog.models import Category
from config.settings import CACHE_ENABLED


def category_selection(queryset):
    return queryset.all()


def cache_category() -> object:
    if CACHE_ENABLED:
        key = 'category_list'
        queryset = cache.get(key)
        if queryset is None:
            queryset = Category.objects.all()
            cache.set(key, queryset, 60)
    else:
        queryset = Category.objects.all()
    return queryset
