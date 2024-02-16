"""
Создайте три модели Django: клиент, товар и заказ.
      ○ Клиент может иметь несколько заказов.
      ○ Заказ может содержать несколько товаров.
      ○ Товар может входить в несколько заказов.

    Поля модели «Товар»:
        — название товара
        — описание товара
        — цена товара
        — количество товара
        — дата добавления товара

    Поля модели «Заказ»:
        — связь с моделью «Клиент», указывает на клиента, сделавшего заказ
        — связь с моделью «Товар», указывает на товары, входящие в заказ
        — общая сумма заказа
        — дата оформления заказа
"""

from django.db import models

"""
Поля модели «Клиент» (client):
    — имя клиента
    — электронная почта клиента
    — номер телефона клиента
    — адрес клиента
    — дата регистрации клиента
"""
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    age = models.IntegerField()
    def __str__(self):
        return f'Username: {self.name}, email: {self.email}, age: {self.age}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)