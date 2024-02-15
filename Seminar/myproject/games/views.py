import random
from django.shortcuts import render
from django.http import HttpResponse
import logging
from games.models import Heads_or_tails

logger = logging.getLogger(__name__)

http_text_hand = "<h3> << Приложение 2 (myapp_2 / Games) >> </h3>"
http_menu = "<h3>МЕНЮ</h3>\
        <a href='/'>Главная</a><br>\
        <a href='/games/heads_or_tails/'>Орел или решка</a><br>\
        <a href='/games/playing_dice/'>Бросай кубик</a><br>\
        <a href='/games/random_100/'>Случайное число от 0 до 100</a><br>\
        <a href='/games/statistic/'>Статистика последних N бросков кубика (10 - по умолчанию)</a><br>"

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
    http_text = result + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)


""" далее используем стандартный вызов логгера """
def heads_or_tails(request):
    result = random.choice(["Орел", "Решка"])
    logger.info(f" - вызвана функция {heads_or_tails.__name__}")
    logger.info(f" >> результат: {result}")
    record = Heads_or_tails(side=result)
    record.save()
    http_text = result + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)

def playing_dice(request):
    result = f"На кубике выпала грань = {random.randint(1,6)}"
    logger.info(f" - вызвана функция {playing_dice.__name__}")
    logger.info(f" >> результат: {result}")
    http_text = result + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)

def random_100(request):
    result = f"Случайное число от 0 до 100 = {random.randint(0,100)}"
    logger.info(f" - вызвана функция {random_100.__name__}")
    logger.info(f" >> результат: {result}")
    http_text = result + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)

def statistic(request, n):
    result = Heads_or_tails.get_N_last_flip(n)
    result = f"Статистика последних {n} бросков игрального кубика: {result}"
    logger.info(f" - вызвана функция {random_100.__name__}")
    logger.info(f" >> результат: {result}")
    http_text = result + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)