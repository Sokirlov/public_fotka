from django.contrib import admin
from .models import Services, Clients, Income, Payments, PaymentsCategory, ClientSource, Administrators
apps_name = 'Бухгалтерия'

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'idSort',]
    list_editable = ['name', 'price', 'idSort',]
admin.site.register(Services, ServicesAdmin)

class ClientSourceAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'name',)
    list_display = ['id', 'name', ]
    ordering = ['id']
admin.site.register(ClientSource, ClientSourceAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display_links = ('date', 'name', 'email', 'tel',)
    list_display = ['id', 'date', 'name', 'email', 'tel', 'comments', 'sourceClient',]
    list_editable = ['comments',]
    search_fields = ['tel',]
    ordering = ['-date']
    list_filter = ('sourceClient',)
admin.site.register(Clients, ClientsAdmin)

class IncomeAdmin(admin.ModelAdmin):
    list_display_links = ('id', 'date_create_order', 'tel', 'service', 'date_ordering',)
    list_display = ['id', 'date_create_order', 'tel', 'service', 'date_ordering', 'comments', 'fineshed']
    list_editable = [ 'fineshed',]
    ordering = ['-date_create_order']
    list_filter = ('date_ordering', 'tel',)
    autocomplete_fields = ['tel']
admin.site.register(Income, IncomeAdmin)


class PaymentsCategoryAdmin(admin.ModelAdmin):
    list_display_links = ('id',)
    list_display = ['id', 'category']
admin.site.register(PaymentsCategory, PaymentsCategoryAdmin)

class PaymentsAdmin(admin.ModelAdmin):
    list_display = ['category', 'date_create_payment', 'payer', 'pay_name', 'payment']
    ordering = ['-date_create_payment']
    list_filter = ('category', 'date_create_payment', 'payer', 'pay_name', 'payment')
admin.site.register(Payments, PaymentsAdmin)

class AdministratorsAdmin(admin.ModelAdmin):
    list_display_links = ('name', 'tel', 'viber', 'telegram', 'whatsapp', 'site', 'fb', 'insta', 'cardNumber',)
    list_display = ['idSort', 'name', 'tel', 'viber', 'telegram', 'whatsapp', 'site', 'fb', 'insta', 'cardNumber']
    list_editable = ['idSort', ]
    ordering = ['idSort']
admin.site.register(Administrators, AdministratorsAdmin)

