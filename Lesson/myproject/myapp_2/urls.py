from django.urls import path
from . import views

urlpatterns = [
    path('supertest/', views.supertest, name='supertest'),
]