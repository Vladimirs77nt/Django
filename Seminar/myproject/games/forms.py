from django import forms

class RandomGames(forms.Form):
    games_choice = (('heads_or_tails', 'Орел или решка'), ('playing_dice', 'Игральная кость'), ('random_100', 'Случайное число'))
    game = forms.ChoiceField(choices=games_choice, label="Выберите игру")
    count = forms.IntegerField(min_value=1, max_value=64, initial=1, label="Колиество попыток")