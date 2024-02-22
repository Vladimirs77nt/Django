from django.shortcuts import render
from django.http import HttpResponse

http_text_hand = "<h3> << Приложение 1 (myapp) >> </h3>"
http_menu = "<h3>МЕНЮ</h3>\
        <a href='/'>Главная</a><br>\
        <a href='/about/'>Страница 'О нас'</a><br>\
        <a href='/supertest/'>Супертест!</a><br>\
        <a href='/games/'>Приложение 2 = Games/Игры</a><br>"

def index(request):
    text = "Привет, мир!"
    return render(request, 'myapp/index.html', {'text': text})

def about(request):
    text = "Страница 'О нас'"
    http_text = text + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)

def supertest(request):
    text = "!!! СУПЕР ТЕСТ !!!"
    http_text = text + "\n" + http_text_hand + http_menu
    return HttpResponse(http_text)