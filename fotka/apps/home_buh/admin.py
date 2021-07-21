from django.contrib import admin
from .models import Categories, Operations

class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['categoryName', 'operations']
    ordering = ['categoryName']
admin.site.register(Categories, CategoriesAdmin)

class OperationsAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'categoryId')
    list_display = ['opertime', 'name', 'categoryId', 'operations', 'summa', 'owner']
    list_editable = ['opertime', 'owner', ]
    ordering = ['-opertime', 'categoryId', 'operations']
    list_filter = ('owner',)
admin.site.register(Operations, OperationsAdmin)