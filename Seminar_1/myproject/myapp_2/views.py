import random
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

def my_logger (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f" -- вызвана функция {func.__name__}")
        logger.info(result)
        return result
    return wrapper


@my_logger
def games_index(request):
    result = 'Index page "Games" accessed'
    return HttpResponse(result)

@my_logger
def heads_or_tails(request):
    result = random.choice(["Орел", "Решка"])
    return HttpResponse(result)

@my_logger
def playing_dice(request):
    result = f"На кубике выпала грань = {random.randint(1,6)}"
    return HttpResponse(result)

@my_logger
def random_100(request):
    result = f"Случайное число от 0 до 100 = {random.randint(0,100)}"
    return HttpResponse(result)