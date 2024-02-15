from django.core.management.base import BaseCommand
from blogs.models import Author

class Command(BaseCommand):
    help = "Get all author."
    
    def handle(self, *args, **kwargs):
        authors = Author.objects.all()
        text_authors = 'All authors:\n'
        for author in authors:
            text_authors += f"{author}" + '\n'
        self.stdout.write(text_authors)