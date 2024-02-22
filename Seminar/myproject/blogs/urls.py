from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogs_index, name='blogs_index'),
    path('author/<int:author_id>/', views.author_posts, name='author_posts'),
    path('post/<int:post_id>/', views.post_full, name='post_full'),
]