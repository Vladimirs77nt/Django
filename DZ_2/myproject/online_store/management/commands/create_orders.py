from datetime import date
import datetime
from random import randint, choice
from django.core.management.base import BaseCommand
from online_store.models import Client, Product, Order
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Orders (random)"

    def handle(self, *args, **kwargs):
        clients = Client.objects.all()
        products = Product.objects.all()

        for client in clients:
            order = Order(client=client,
                          total_price=0,
                          date_ordered=date(year=randint(2022,2023), month=randint(1,12), day=randint(1,30)))
            order.save()
            total_price = 0
            for i in range(randint(0,5)):   # от 0 до 4 товаров в заказе
                product = choice(products)
                order.products.add(product)
                order.save()
                total_price += product.price
            order.total_price = total_price
            order.save()
            print (order)

        self.stdout.write(f'All orders - created')