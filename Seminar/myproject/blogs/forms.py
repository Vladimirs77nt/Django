from django import forms
from .models import Author, Post, Comment

# ----------------------------------------------------------------------------------------------------------
# Задание №3
#     Продолжаем работу с авторами, статьями и комментариями.
#     Создайте форму для добавления нового автора в базу данных.
#     Используйте ранее созданную модель Author

class AuthorForm (forms.ModelForm):
    class Meta:
        model = Author
        # fields = ['name', 'surname', 'email', 'biography', 'birthday']                  
        exclude = ['full_name']
        labels = {'name': 'Имя',
                  'surname': 'Фамилия',
                  'email': 'Электронная почта',
                  'biography': 'Биография',
                  'birthday': 'День рождения',
                  }
# ----------------------------------------------------------------------------------------------------------
# Задание №4
#     Аналогично автору создайте форму добавления новой статьи.
#     Автор статьи должен выбираться из списка (все доступные в базе данных авторы).
        
class PostForm (forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Выберите автора")
    title = forms.CharField(min_length=1, label="Заголовок")
    content = forms.CharField(widget=forms.Textarea, label="Текст статьи")
    category = forms.CharField(min_length=1, label="Категория")
    ispublic = forms.BooleanField(required=False, label="опубликовать сразу")

# ----------------------------------------------------------------------------------------------------------
# Задание №5
#     Доработаем задачу 6 из прошлого семинара.
#     Мы сделали вывод статьи и комментариев.
#     Добавьте форму ввода нового комментария в существующий шаблон.
        
class CommentForm (forms.Form):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), label="Выберите автора")
    content = forms.CharField(widget=forms.Textarea, label="комментарий")