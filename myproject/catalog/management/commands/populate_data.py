from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_data():
        with open('fixtures/catalog_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
        return data

    def handle(self, *args, **options):
        # Удаление всех объектов из базы данных
        Category.objects.all().delete()
        Product.objects.all().delete()

        # Создание категорий
        data = self.json_read_data()
        for item in data:
            if item['model'] == 'catalog.category':
                category_data = item['fields']
                Category.objects.create(
                    pk=item['pk'],
                    name=category_data['name'],
                    description=category_data['description']
                )

        # Создание продуктов
        for item in data:
            if item['model'] == 'catalog.product':
                product_data = item['fields']
                category_id = product_data['category']
                try:
                    category = Category.objects.get(pk=category_id)
                except Category.DoesNotExist:
                    print(f"Category with pk '{category_id}' does not exist in the database.")
                    continue

                Product.objects.create(
                    pk=item['pk'],
                    name=product_data['name'],
                    description=product_data['description'],
                    category=category,
                    price=product_data['price']
                )
