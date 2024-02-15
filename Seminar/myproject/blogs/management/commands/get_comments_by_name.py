"""
Задание №7

Создайте функции для работы с базой данных:
    ○ Поиск всех статей автора по его имени
    ○ Поиск всех комментариев автора по его имени
    ○ Поиск всех комментариев по названию статьи

Каждая из трёх функций должна иметь возможность сортировки и ограничение выборки по количеству.

"""

from django.core.management.base import BaseCommand
from blogs.models import Post, Author, Comment

class Command(BaseCommand):
    help = "Get all comments by name author."
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Name author')
    
    def handle(self, *args, **kwargs):
        name = kwargs['name']
        comments = Comment.objects.all()
        result = ""
        for comment in comments:
             if comment.author.name == name:
                 result += f"{comment}\n"
        self.stdout.write(result)