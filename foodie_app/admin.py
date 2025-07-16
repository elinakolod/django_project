from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'date_added')
    search_fields = ('id', 'name')

admin.site.register(Category, CategoryAdmin)
