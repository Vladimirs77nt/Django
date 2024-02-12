import random
from django.shortcuts import render
from django.http import HttpResponse

def heads_or_tails(request):
    if random.randint(0,1):
        return HttpResponse("Орел")
    else:
        return HttpResponse("Решка")
    
def playing_dice(request):
    return HttpResponse(f"На кубике выпала грань = {random.randint(1,6)}")

def random_100(request):
    return HttpResponse(f"Случайное число от 0 до 100 = {random.randint(0,100)}")