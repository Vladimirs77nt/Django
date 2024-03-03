from django.contrib import admin
from .models import Heads_or_tails

# СПОСОБ 2 - на семинаре
@admin.register(Heads_or_tails)
class Heads_or_tails_Admin(admin.ModelAdmin):
    pass


# СПОСОБ 1 - из лекции
    # admin.site.register(Heads_or_tails)