from datetime import date
import random
from django.core.management.base import BaseCommand
from online_store.models import Product
import faker    # генерация фейковых имен и фамилий

fake = faker.Faker('ru_RU')

class Command(BaseCommand):
    help = "Create Product"

    def handle(self, *args, **kwargs):
        for i in range(10):
            id_latest = Product.objects.latest("pk")
            product = Product(name=f'Product_{id_latest}-{random.randint(1,1000)}',
                              description=fake.paragraph(nb_sentences=5),
                              price = random.randint(1,1000),
                              quantity = random.randint(1,100),
                              date_add = date(year=random.randint(2020,2023), month=random.randint(1,12), day=random.randint(1,30)))
            # id_latest = product.pk
            # product.name = f'Product_{id_latest}-{random.randint(1,1000)}'
            product.save()
            self.stdout.write(f'Create product [id:{product.pk}]: {product}')