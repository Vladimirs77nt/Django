from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_index, name='blogs_index'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
    path('posts_all/', views.posts_all, name='posts_all'),
    path('authors_all/', views.authors_all, name='authors_all'),
    path('author_form/', views.author_form, name='author_form'),
    path('post_form/', views.post_form, name='post_form'),
]