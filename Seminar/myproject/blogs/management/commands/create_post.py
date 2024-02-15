from datetime import date
from random import randint, choice
from django.core.management.base import BaseCommand
from blogs.models import Author, Post
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Post"

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        title = lorem_ipsum.words(5, common = False).capitalize()
        content = "\n".join(lorem_ipsum.paragraphs(7, common=False))
        date_pub = date(year=randint(2020,2023), month=randint(1,12), day=randint(1,30))
        author = choice(authors)
        category = choice(lorem_ipsum.WORDS).capitalize()

        post = Post(title=title,
                    content=content,
                    date_pub=date_pub,
                    author=author,
                    category=category)
        post.save()
        self.stdout.write(f'Create post [{post.pk}]: {post.title}')