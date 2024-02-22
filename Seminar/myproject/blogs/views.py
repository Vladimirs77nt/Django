import logging
from django.http import HttpResponse
from blogs.models import Author, Post, Comment
from django.shortcuts import get_object_or_404, render


logger = logging.getLogger(__name__)

def blogs_index(request):
    text = 'Index page "Blogs Start" accessed'
    logger.info(text)
    return render(request, 'blogs/blogs_index.html', {'text': text})

def blogs(request):
    result = 'Index page "Blogs" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def author(request):
    result = 'Index page "Author" accessed'
    logger.info(result)
    http_text = result + "\n"
    return HttpResponse(http_text)

def author_posts(request, author_id):
    author = get_object_or_404(Author, pk=author_id)
    posts = Post.objects.filter(author=author)
    print (*posts)
    return render(request, 'blogs/author_posts.html', {'author': author, 'posts': posts})

def post_full(request, post_id):
    post_get = get_object_or_404(Post, pk=post_id)
    author = post_get.author
    comments = Comment.objects.filter(post=post_get).order_by('-date_create')
    post_get.views_count += 1
    post_get.save()
    return render(request, 'blogs/post_full.html', {'post': post_get, 'author': author, 'comments': comments})