from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_index, name='games_index'),
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('playing_dice/', views.playing_dice, name='playing_dice'),
    path('random_100/', views.random_100, name='random_100'),
]