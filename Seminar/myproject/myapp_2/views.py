import random
from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

""" декоратор-логгер записи вызванной функции """
def my_logger (func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.info(f" -- вызвана функция {func.__name__}")
        return result
    return wrapper

""" использование логгера для главной страницы """
@my_logger
def games_index(request):
    result = 'Index page "Games" accessed'
    logger.info(result)
    return HttpResponse(result)

""" далее используем стандартный вызов логгера """
def heads_or_tails(request):
    result = random.choice(["Орел", "Решка"])
    logger.info(f" - вызвана функция {heads_or_tails.__name__}")
    logger.info(f" >> результат: {result}")
    return HttpResponse(result)

def playing_dice(request):
    result = f"На кубике выпала грань = {random.randint(1,6)}"
    logger.info(f" - вызвана функция {playing_dice.__name__}")
    logger.info(f" >> результат: {result}")
    return HttpResponse(result)

def random_100(request):
    result = f"Случайное число от 0 до 100 = {random.randint(0,100)}"
    logger.info(f" - вызвана функция {random_100.__name__}")
    logger.info(f" >> результат: {result}")
    return HttpResponse(result)