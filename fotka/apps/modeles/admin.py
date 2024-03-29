from django.contrib import admin
from .models import Modeles

@admin.register(Modeles)
class ModelesAdmin(admin.ModelAdmin):
    list_display_links = ('fio', 'sex', 'lenth', 'weight', 'money',)
    list_editable = ['insta', 'fb', ]
    list_display = ('id', 'image_tag', 'fio', 'sex', 'lenth', 'weight', 'insta', 'fb',  'money', 'tfp',)
    ordering = ['date',]
    list_filter = ('lenth', 'weight', 'chest', 'waist', 'hips', 'footwear', 'hair_color', 'haer_lenth', 'money',)
    readonly_fields = ('image_tag',)
