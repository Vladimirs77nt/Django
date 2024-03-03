from django.contrib import admin
from .models import Author, Post, Comment

# СПОСОБ 2 - на семинаре
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'surname', 'birthday']
    list_filter = ['id', 'name', 'surname']
    list_sort = ['id', 'fullname', 'birthday']

    fieldsets = [(None,
                    {'classes': ['wide'],
                     'fields': ['name', 'surname', 'birthday', 'fullname'],
                    },
                ),
                ('Подробности:',
                    {'classes': ['collapse'],
                     'description': 'Полная информация',
                     'fields': ['email', 'biography'],
                    },
                ),
            ]
    
    # не изменяемые поля
    readonly_fields = ['fullname', 'birthday', 'email']

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author', 'ispublic']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['author', 'post']

# СПОСОБ 1 - из лекции
    # admin.site.register(Post)
    # admin.site.register(Comment)
