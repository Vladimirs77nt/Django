from django.urls import path
from . import views

urlpatterns = [
    path('', views.games_index, name='games_index'),
    path('heads_or_tails/', views.heads_or_tails, name='heads_or_tails'),
    path('playing_dice/', views.playing_dice, name='playing_dice'),
    path('random_100/', views.random_100, name='random_100'),
    path('statistic/<int:n>', views.statistic, name='statistic'),

    path('heads_or_tails/<int:count>/', views.heads_or_tails_count, name='heads_or_tails_count'),
    path('playing_dice/<int:count>/', views.playing_dice_count, name='playing_dice_count'),
    path('random_100/<int:count>/', views.random_100_count, name='random_100_count'),
    path('select_game/', views.select_game, name='select_game'),
]