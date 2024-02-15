from django.core.management.base import BaseCommand
from blogs.models import Post

class Command(BaseCommand):
    help = "Get all post."
    
    def handle(self, *args, **kwargs):
        posts = Post.objects.all()
        text_post = 'All posts (title):\n'
        for post in posts:
            text_post += f"{post}" + '\n'
        self.stdout.write(text_post)