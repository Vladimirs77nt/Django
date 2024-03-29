from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
http_text_hand = "<h1>Приветствую вас!</h1>"
http_text_footer = "<p>GeekBrains – образовательный портал. Мы учим людей с нуля осваивать программирование, веб-дизайн, маркетинг и другие\
              современные профессии. Проводим онлайн-курсы со стажировкой и бесплатные мастер-классы, развиваем сообщество, \
                сотрудничаем с компаниями по трудоустройству и непрерывно тестируем новые методики для поднятия эффективности\
                      обучения.\
                        У нас есть направления и для детей – GeekSchool. GeekSchool — это школа программирования и цифрового творчества для ребят 7-17 лет. Мы помогаем освоить цифровые навыки, расширить кругозор и найти перспективную профессию. Ребята в GeekSchool создают игры, рисуют персонажей, придумывают сюжеты, пишут код для создания сайтов, приложений и чат-ботов и делают крутые проекты с помощью компьютера.</p>"
http_menu = "<h3>МЕНЮ</h3>\
        <a href='/'>Главная</a><br>\
        <a href='/about/'>Обо мне</a><br>"

def index(request):
    title = "<h2>Вы находитесь на главной странице</h2>"
    title_2 = "<h3>На нашем сайте вы можете познакомится с программированием</h3>"
    http_text = http_text_hand + http_menu + title + title_2 + http_text_footer
    logger.info(f" >> посещена главная страница /index")
    return HttpResponse(http_text)

def about(request):
    title = "<h2>Вы находитесь на странице 'Обо мне'</h2>"
    title_2 = "<h3>Давайте познакомимся. Меня зовут Владимир, я студент GeekBrains</h3>"
    title_3 = "<p>Сейчас работаю инженером-конструктором рекламных конструкций (работа с дизайном, графикой и программами\
        для проектирования) + иногда работа с табличными данными и их анализом. Дополнительно проходу обучение на \
          программиста/разработчика, технологическая специализация - веб-разработка на Python, школа GeekBrains. \
            Изучал и писал учебные программы на Java, Python, C#, Прошел курс ООП (на Java и Python), изучал Linux, \
            Git, компьютерные сети, базы данных MySQL. Сейчас прохожу изучение веб-верстки, архитектура ПО, \
              фреймворков Flask/FastAPI и Django. Осталось +/- 1-2 месяца учебы.\
                Репозиторий Github с учебными заданиями:\
                  https://github.com/Vladimirs77nt</p>"
    

    http_text = http_text_hand + http_menu + title + title_2 + title_3 + http_text_footer
    logger.info(f" >> посещена страница 'обо мне'/about")
    return HttpResponse(http_text)