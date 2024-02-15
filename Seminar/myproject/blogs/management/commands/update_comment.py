from django.core.management.base import BaseCommand
from blogs.models import Post, Comment

class Command(BaseCommand):
    help = "Update comment Content by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Comment ID')
        parser.add_argument('content', type=str, help='Comment content')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        content = kwargs.get('content')
        comment = Comment.objects.filter(pk=pk).first()
        comment.content = content
        comment.save()
        self.stdout.write(f'Udate comment: {comment}')