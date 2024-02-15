from django.core.management.base import BaseCommand
from blogs.models import Author

class Command(BaseCommand):
    help = "Get author by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
    
    def handle(self, *args, **kwargs):

        # id = kwargs['id']
        pk = kwargs['pk']

        # author = Author.objects.get(id=id)
        author = Author.objects.filter(pk=pk).first()

        self.stdout.write(f'{author}')