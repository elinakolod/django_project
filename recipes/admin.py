from django.contrib import admin
from .models import Recipe

class ReceipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'date_added')
    search_fields = ('id', 'name', 'category__name')

admin.site.register(Recipe, ReceipeAdmin)
