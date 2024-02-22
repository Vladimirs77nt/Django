from django.db import models

"""
модель Автор:
    ○ имя до 100 символов
    ○ фамилия до 100 символов
    ○ почта
    ○ биография
    ○ день рождения
"""
class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField()
    birthday = models.DateField()
    full_name = models.CharField(max_length=200)

    def fullname (self):
        return f"{self.surname} {self.name}"

    def __str__(self):
        return f'Author [{self.pk}], {self.surname} {self.name}, email: {self.email}, birthday: {self.birthday}'

"""  модель Статья (публикация).
Авторы из прошлой задачи могут писать статьи.
У статьи может быть только один автор.
У статьи должны быть следующие обязательные поля:
    ○ заголовок статьи с максимальной длиной 200 символов
    ○ содержание статьи
    ○ дата публикации статьи
    ○ автор статьи с удалением связанных объектов при удалении автора
    ○ категория статьи с максимальной длиной 100 символов
    ○ количество просмотров статьи со значением по умолчанию 0
    ○ флаг, указывающий, опубликована ли статья со значением по умолчанию False 
"""
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_pub = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.CharField(max_length=100)
    views_count = models.IntegerField(default=0)
    ispublic = models.BooleanField(default=False)
    
    def __str__(self):
        words = self.content.split()
        return f'Post [{self.pk}], author: {self.author.full_name}, title: {self.title} |  content: {" ".join(words[:8])}...'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:8])}...'
    
"""  модель Комментарий (публикация).
Авторы могут добавлять комментарии к своим и чужим статьям.
Т.е. у комментария может быть один автор. И комментарий относится к одной статье.
У модели должны быть следующие поля:
    ○ автор
    ○ статья
    ○ комментарий
    ○ дата создания
    ○ дата изменения
"""
class Comment(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    date_create = models.DateField()
    date_edit = models.DateField()
    
    def __str__(self):
        words = self.content.split()
        return f'Comment [{self.pk}], post: {self.post.title} | author: {self.author.name} |  comment: {" ".join(words[:8])}...'
    
    def get_summary(self):
        words = self.content.split()
        return f'{" ".join(words[:12])}...'