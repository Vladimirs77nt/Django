from django.core.management.base import BaseCommand
from blogs.models import Comment

class Command(BaseCommand):
    help = "Get all comments."
    
    def handle(self, *args, **kwargs):
        comments = Comment.objects.all()
        text_comments = 'All comments:\n'
        for comment in comments:
            text_comments += f"{comment}" + '\n'
        self.stdout.write(text_comments)