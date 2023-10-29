from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class AdminMenu(admin.ModelAdmin):
    list_display = 'id', 'title', 'parent', 'named_url', 'menu_name'
