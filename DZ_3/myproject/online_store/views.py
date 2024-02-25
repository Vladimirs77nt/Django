import logging
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from online_store.models import Client, Order

logger = logging.getLogger(__name__)

def store_index(request):
    text = 'Index page "Online Store Start" accessed'
    logger.info(text)   
    return render(request, 'online_store/store_index.html', {'text': text})

def clients_all(request):
    clients = Client.objects.all()
    logger.info('Index page "Client ALL" accessed')
    return render(request, 'online_store/clients_all.html', {'clients': clients})

def client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id)
    logger.info('Index page "Client" accessed')
    return render(request, 'online_store/client.html', {'client': client, 'orders': orders})

def product(request):
    result = 'Index page "Product" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def order(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    products_in_order = order.products.all()
    return render(request, 'online_store/order.html', {'order': order, 'products_in_order': products_in_order})


"""
Задание №7 (с семинара)
    Доработаем задачу 8 из прошлого семинара про клиентов, товары и заказы.
    Создайте шаблон для вывода всех заказов клиента и списком товаров внутри каждого заказа.
    Подготовьте необходимый маршрут и представление.
"""
def orders_by_client(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id)
    return render(request, 'online_store/orders_no_sort.html', {'orders': orders, 'client': client})


"""
Домашнее задание:
    Продолжаем работать с товарами и заказами.
    Создайте шаблон, который выводит список заказанных клиентом товаров
    из всех его заказов с сортировкой по времени:
        * за последние 7 дней (неделю)
        * за последние 30 дней (месяц)
        * за последние 365 дней (год)
    * Товары в списке не должны повторятся.
"""
def orders_by_client_sort(request, client_id):
    client = get_object_or_404(Client, pk=client_id)
    orders = Order.objects.filter(client__pk=client_id)
    return render(request, 'online_store/orders_sort.html', {'orders': orders, 'client': client})