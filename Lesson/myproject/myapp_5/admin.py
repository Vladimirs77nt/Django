from django.contrib import admin
from .models import Category, Product


# метод сбрасывания количества товаров в ноль
@admin.action(description="Сбросить количество в ноль")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)


class ProductAdmin(admin.ModelAdmin):

    # отображение столбцов
    list_display = ['name', 'category', 'quantity']

    # ВАРИАНТ 1
    # новое поле fields определяет порядок вывода элементов формы
    # eсли опустить какие-то поля, они перестанут отображаться
    # например мы больше не видим цену и количество товара
        # fields = ['name', 'description', 'category', 'date_added', 'rating']
    
    # ВАРИАНТ 2
    fieldsets = [(None,
                    {
                        'classes': ['wide'],
                        'fields': ['name'],
                        },
                    ),
                ('Подробности',
                    {
                        'classes': ['collapse'],
                        'description': 'Категория товара и его подробное описание',
                        'fields': ['category', 'description'],
                        },
                    ),
                ('Бухгалтерия',
                    {
                        'fields': ['price', 'quantity'],
                        }
                    ),
                ('Рейтинг и прочее',
                    {
                        'description': 'Рейтинг сформирован автоматически на основе оценок покупателей',
                        'fields': ['rating', 'date_added'],
                        }
                    ),
                ]
    
    # не изменяемые поля
    readonly_fields = ['date_added', 'rating']

    # сортировка
    ordering = ['category', '-quantity']

    # фильтрация
    list_filter = ['date_added', 'price']

    # текстовый поиск
    search_fields = ['description']
    search_help_text = 'Поиск по полю Описание продукта (description)'

    # Чтобы действие появилось в списке возможных, прописываем у административной
    # модели переменную actions. В список складываем добавляемые действия.
    actions = [reset_quantity]

# связь модели Product с админской настройкой (класс) ProductAdmin
admin.site.register(Product, ProductAdmin)

admin.site.register(Category)