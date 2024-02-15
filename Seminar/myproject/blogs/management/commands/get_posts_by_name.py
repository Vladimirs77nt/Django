"""
Задание №7

Создайте функции для работы с базой данных:
    ○ Поиск всех статей автора по его имени
    ○ Поиск всех комментариев автора по его имени
    ○ Поиск всех комментариев по названию статьи

Каждая из трёх функций должна иметь возможность сортировки и ограничение выборки по количеству.

"""

from django.core.management.base import BaseCommand
from blogs.models import Post

class Command(BaseCommand):
    help = "Get all posts by name author."
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name author')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        posts = Post.objects.all()
        result = ""
        for post in posts:
             if post.author.name == name:
                 result += f"{post}\n"
        self.stdout.write(result)