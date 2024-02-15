from django.core.management.base import BaseCommand
from blogs.models import Post

class Command(BaseCommand):
    help = "Update post TITLE by id."
    
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='Post ID')
        parser.add_argument('title', type=str, help='Post title')

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        title = kwargs.get('title')
        post = Post.objects.filter(pk=pk).first()
        post.title = title
        post.save()
        self.stdout.write(f'Udate post: {post}')