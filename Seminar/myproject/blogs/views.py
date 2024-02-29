import datetime
import logging
from django.http import HttpResponse

from django.shortcuts import get_object_or_404, render, redirect
from .forms import AuthorForm, PostForm, CommentForm
from .models import Author, Post, Comment

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
    return render(request, 'blogs/author_posts.html', {'author': author, 'posts': posts})

def posts_all(request):
    posts = Post.objects.all()
    return render(request, 'blogs/posts_all.html', {'posts': posts})

def authors_all(request):
    authors = Author.objects.all()
    return render(request, 'blogs/authors_all.html', {'authors': authors})

# ----------------------------------------------------------------------------------------------------------
# Семинар 4

# Задание №5
    # Доработаем задачу 4.
    # Создай шаблон для вывода подробной информации о статье.
    # Внесите изменения в "views.py" - создайте представление и в "urls.py" - добавьте маршрут.
    #  * Увеличивайте счётчик просмотра статьи на единицу при каждом просмотре

# Задание №6
    # Измените шаблон для вывода заголовка и текста статьи, а также всех комментариев к статье с указанием текста
    # комментария, автора комментария и даты обновления комментария в хронологическом порядке.
    # Если комментарий изменялся, дополнительно напишите “изменено”.
    # Не забывайте про представление с запросом в БД и маршруты. Проверьте, что они работают верно

# Семинар 4
# Задание №5
    # Доработаем задачу 6 из прошлого семинара.
    # Мы сделали вывод статьи и комментариев.
    # Добавьте форму ввода нового комментария в существующий шаблон.

def post_full(request, post_id):
    post_get = get_object_or_404(Post, pk=post_id)
    author = post_get.author
    comments = Comment.objects.filter(post=post_get).order_by('-date_create')
    post = {'title':post_get.title,
            'date_pub': post_get.date_pub,
            'content':post_get.content}
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            comment = Comment(author = author,
                              content = content,
                              post = post_get
                              )
            comment.save()
            return redirect('post_full', post_id)
    else:
        form = CommentForm()

    post_get.views_count += 1
    post_get.save()
    return render(request, 'blogs/post_full.html', {'post': post_get, 'author': author, 'comments': comments, 'form':form})

# ----------------------------------------------------------------------------------------------------------
# Семинар 4
# Задание №3
#     Продолжаем работу с авторами, статьями и комментариями.
#     Создайте форму для добавления нового автора в базу данных.
#     Используйте ранее созданную модель Author
def author_form(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            form.save()
            message = 'Автор сохранен'
            return redirect('author_form')
    else:
        form = AuthorForm()
        message = 'Заполните форму'
    return render(request, 'blogs/author_form.html', {'form':form, 'message':message})

# Семинар 4
# Задание №4
#     Аналогично автору создайте форму добавления новой статьи.
#     Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
def post_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        message = 'Ошибка в данных'
        if form.is_valid():
            author = form.cleaned_data['author']
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            category = form.cleaned_data['category']
            ispublic = form.cleaned_data['ispublic']
            date_pub = datetime.date.today()
            post = Post(author = author,
                        title = title,
                        content = content,
                        category = category,
                        ispublic = ispublic,
                        date_pub = date_pub)
            post.save()
            message = 'Статья сохранена'
            return redirect('post_form')
    else:
        form = PostForm()
        message = 'Заполните форму'
    return render(request, 'blogs/post_form.html', {'form':form, 'message':message})