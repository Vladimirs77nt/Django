from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_index, name='store_index'),
    path('client/', views.blogs, name='client'),
    path('product/', views.author, name='product'),
    path('order/', views.author, name='order'),
]