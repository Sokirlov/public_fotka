from django.contrib import admin
from .models import Zakaz

@admin.register(Zakaz)
class ZakazAdmin(admin.ModelAdmin):
    list_display = ('name', 'comments', 'pagelink', 'status', 'email', 'tel', 'zakazTime',)
    list_editable = ['status']
    ordering = ['status', '-zakazTime',]
    list_filter = ('status',)

