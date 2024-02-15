from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_index, name='blogs_index'),
    path('blogs/', views.blogs, name='blogs'),
    path('author/', views.author, name='author'),
]