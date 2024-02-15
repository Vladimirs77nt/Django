from django.core.management.base import BaseCommand
from blogs.models import Author

class Command(BaseCommand):
    help = "Update author NAME by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Author ID')
        parser.add_argument('name', type=str, help='Author name')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        name = kwargs.get('name')
        author = Author.objects.filter(pk=pk).first()
        author.name = name
        surname = author.surname
        author.fullname = f"{name} {surname}"
        author.save()
        self.stdout.write(f'Udate author: {author}')