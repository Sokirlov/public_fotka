from django import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Zakaz
from photo.models import Category, Price

class ZakazForm(forms.ModelForm):
    pagelink = forms.ModelChoiceField(queryset=Price.objects.all(), label='', empty_label=_("Выбирите услугу"))

    class Meta:
        model = Zakaz
        fields = ('name', 'email', 'tel', 'pagelink', 'comments',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Имя'), 'class': 'form_name'}),
            'email': forms.TextInput(attrs={'placeholder': _('Емэил'), 'class': 'form_email'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form_tel'}),
            'comments': forms.Textarea(attrs={'placeholder': _('Опишите ваш заказ')}),
        }
        labels = {
            'name': '',
            'email': '',
            'tel': '',
            'comments': '',
        }