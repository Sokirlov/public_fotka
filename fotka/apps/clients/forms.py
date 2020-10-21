from django.core import validators
from django.core.validators import validate_email
from django import forms
from django.utils.translation import gettext_lazy as _
from clients.models import Zakaz
from photo.models import Category, Globals, Price



class ZakazForm(forms.ModelForm):
    # pagelink = forms.ModelChoiceField(queryset=Category.objects.all().only('categoryName'), label='', empty_label = _("Выбирите услугу"))
    # def __init__(self, *args, **kwargs):
    #     super(ZakazForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'].queryset = Category.objects.all().only('categoryName')
    # def get_absolute_url(self):
    #     return reverse('photo:detail', kwargs = {'razdel': self.razdel, 'slug': self.slug,})
    pagelink = forms.ModelChoiceField(queryset=Category.objects.all(), label='', empty_label = _("Выбирите услугу"))
    # pagelink = forms.ModelChoiceField(queryset=Price.objects.all(), label='', empty_label=_("Выбирите услугу"))

    # #     return self.kwargs['slug']
    # def __init__(self, *args, **kwargs):
    #     super(ZakazForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'].queryset = Price.objects.all()


    class Meta:
        model = Zakaz
        fields = ('name', 'email', 'tel', 'pagelink', 'comments',)
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': _('Имя'), 'class': 'form_name'}),
            'email': forms.TextInput(attrs={'placeholder': _('Емэил'), 'class': 'form_email'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'class': 'form_tel'}),
            # 'pagelink': forms.Select(),
            'comments': forms.Textarea(attrs={'placeholder': _('Опишите ваш заказ')}),
        }
        labels = {
            'name': '',
            'email': '',
            'tel': '',
            'comments': '',
        }
        # default_validators = [
        #     validators.validate_email
        # ]
    # def __init__(self, *args, **kwargs):
    #     super(ZakazForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'].queryset = Category.objects.all().values_list('slug', 'categoryName')

    # def __init__(self, *args, **kwargs):
    #     super(ChoiceForm, self).__init__(*args, **kwargs)
    #     self.fields['pagelink'] = ModelChoiceField(queryset=Category.objects.all()), empty_label = "Choose a countries",)
