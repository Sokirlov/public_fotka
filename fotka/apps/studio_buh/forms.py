from django import forms
from django.core.exceptions import NON_FIELD_ERRORS
from .models import Income, Payments, Clients
from .views import *


class ClientsForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ('name', 'email', 'tel', 'comments', 'sourceClient')

        error_messages = {
            NON_FIELD_ERRORS: {
                'unique_together': "%(model_name)s's %(field_labels)s are not unique.",
            }
        }

class PaymentsForm(forms.ModelForm):
    class Meta:
        model = Payments
        fields = ('category', 'payer', 'pay_name', 'payment',)


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ('tel', 'service', 'date_ordering', 'order', 'prepay', 'who_admin',)  # 'payment', 'payment_type', 'comments' )

        widgets = {
            'date_ordering': forms.DateTimeInput(format=['%d/%m/%Y']),
        }