from django.contrib import admin
from .models import MenuItem


@admin.register(MenuItem)
class AdminMenu(admin.ModelAdmin):
    list_display = 'title', 'parent', 'url', 'named_url', 'menu_name'
