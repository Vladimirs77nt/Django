from django.core.management.base import BaseCommand
from blogs.models import Comment

class Command(BaseCommand):
    help = "Get comment by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')
    
    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        comment = Comment.objects.filter(pk=pk).first()
        self.stdout.write(f'{comment}')