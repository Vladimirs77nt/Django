from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_index, name='store_index'),
    path('client/<int:client_id>/', views.client, name='client'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('clients_all/', views.clients_all, name='clients_all'),
    path('order/<int:order_id>/', views.order, name='order'),
    path('orders_no_sort/<int:client_id>/', views.orders_by_client, name='orders_by_client'),
    path('orders/<int:client_id>/', views.orders_by_client_sort, name='orders_by_client_sort'),
]