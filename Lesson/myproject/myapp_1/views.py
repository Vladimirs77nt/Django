import random
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, мир!")

def about(request):
    return HttpResponse("Страница 'О нас'")