from django.urls import path
from . import views

urlpatterns = [
    path('', views.store_index, name='store_index'),
    path('client/', views.client, name='client'),
    path('product/', views.product, name='product'),
    path('order/', views.order, name='order'),
]