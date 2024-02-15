from datetime import date
import datetime
from random import randint, choice
from django.core.management.base import BaseCommand
from blogs.models import Author, Post, Comment
from django.utils import lorem_ipsum

class Command(BaseCommand):
    help = "Create Comment"

    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        posts = Post.objects.all()
        content = "\n".join(lorem_ipsum.paragraphs(1, common=False))
        date_create = date(year=randint(2020,2023), month=randint(1,12), day=randint(1,30))
        author = choice(authors)
        post = choice(posts)
        delta = datetime.timedelta(days=randint(0,10))

        comment = Comment(author=author,
                          post=post,
                          content=content,
                          date_create=date_create,
                          date_edit=date_create+delta)
        comment.save()
        self.stdout.write(f'Create comment [{comment.pk}]: {comment}')