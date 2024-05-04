from catalog.models import Category
from django.core.cache import cache


def all_category():
    categories = cache.get('all_categories')
    if not categories:
        categories = Category.objects.all()
        cache.set('all_categories', categories)
    return categories
