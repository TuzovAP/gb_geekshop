import json
from django.core.management.base import BaseCommand
from django.conf import settings
from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product


def load_from_json(file_name):
    with open(f'{settings.BASE_DIR}/json/{file_name}.json', 'r', encoding='utf-8') as json_file:
        return json.load(json_file)

class Command(BaseCommand):
    def handle(self, *args, **options):
        categoties = load_from_json('categories')
        ProductCategory.objects.all().delete()
        for category in categoties:
            ProductCategory.objects.create(**category)

        proructs = load_from_json('products')
        Product.objects.all().delete()
        for product in proructs:
            category_name = product['category']
            category_item = ProductCategory.objects.get(name=category_name)
            product['category'] = category_item
            Product.objects.create(**product)

    ShopUser.objects.create_superuser('django', password='geekbrains', age=18)

