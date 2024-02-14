import random
from django.shortcuts import render
from django.http import HttpResponse

def supertest(request):
    return HttpResponse("СУПЕР ТЕСТ")