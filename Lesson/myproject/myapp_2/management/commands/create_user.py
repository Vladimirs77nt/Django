from django.core.management.base import BaseCommand
from myapp_2.models import User

class Command(BaseCommand):
    help = "Create user."
    
    def handle(self, *args, **kwargs):
        user = User(name='Neo', email='neo@example.com', password='secret', age=58)
        # user = User(name='John', email='john@example.com', password='secret', age=25)
        user.save()
        self.stdout.write(f'{user}')