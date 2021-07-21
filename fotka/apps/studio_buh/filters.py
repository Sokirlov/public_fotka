from .models import PaymentsCategory, Payments
import django_filters

class PaymentsFilter(django_filters.FilterSet):
    class Meta:
        model = Payments
        fields = ['category', 'payer',]