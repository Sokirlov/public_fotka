from modeles.models import Modeles
from django.utils.translation import gettext_lazy as _
from django import forms

from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField

class ModelesForm(forms.ModelForm):

    class Meta:
        model = Modeles

        fields = ('fio', 'tel', 'email', 'insta', 'fb', 'face', 'full_photo', 'sex', 'birthday', 'lenth', 'weight', 'chest', 'waist', 'hips', 'footwear', 'hair_color', 'haer_lenth', 'money', )
        widgets = {
            'fio': forms.TextInput(attrs={'placeholder': _('ФИО'), 'id': 'id_fio'}),
            'tel': forms.TextInput(attrs={'placeholder': _('Телефон'), 'id': 'id_tel', 'pattern': '[\+]?[0-9]{10,12}'}),
            'email': forms.TextInput(attrs={'placeholder': _('Емэил'), 'id': 'id_email'}),
            'insta': forms.TextInput(attrs={'placeholder': _('Ссылка на Instagram'), 'id': 'id_insta'}),
            'fb':  forms.TextInput(attrs={'placeholder': _('Ссылка на Facebook'), 'id': 'id_fb'}),
            'face': forms.FileInput(),
            'full_photo': forms.FileInput(),
            'sex': forms.Select(),
            'birthday': forms.SelectDateWidget(years=range(1980, 2002,), empty_label=('год', 'месяц', 'день',)),# forms.TextInput(attrs={'placeholder': ('День рождения'), 'id': 'id_birthday'}),
            'lenth': forms.TextInput(attrs={'placeholder': _('Рост см, (число)'), 'id': 'id_lenth','pattern':'[0-9]{3}'}),
            'weight': forms.TextInput(attrs={'placeholder': _('Вес в кг, (число)'), 'id': 'id_weight','pattern':'[0-9]{2}'}),
            'chest': forms.TextInput(attrs={'placeholder': _('Объем в груди см, (число)'), 'id': 'id_chest','pattern':'[0-9]{2,3}'}),
            'waist': forms.TextInput(attrs={'placeholder': _('Объем в  талии см, (число)'), 'id': 'id_waist','pattern':'[0-9]{2,3}'}),
            'hips': forms.TextInput(attrs={'placeholder': _('Объем в бедрах см, (число)'), 'id': 'id_hips','pattern':'[0-9]{2,3}'}),
            'footwear': forms.TextInput(attrs={'placeholder': _('Размер обуви, (число)'), 'id': 'id_footwear','pattern':'[0-9]{2}'}),
            'hair_color': forms.Select(),
            'haer_lenth': forms.Select(),
            'money': forms.TextInput(attrs={'placeholder': _('Гонорар в грн, (только число)'), 'id': 'id_money','pattern':'[0-9]{2,6}'}),

        # 'name': forms.TextInput(attrs={'placeholder': ('Имя'), 'class': 'form_name'}),
        #     'email': forms.TextInput(attrs={'placeholder': ('Емэил'), 'class': 'form_email'}),
        #     'tel': forms.TextInput(attrs={'placeholder': ('Телефон'), 'class': 'form_tel'}),
        #     # 'pagelink': forms.Select(),
        #     'comments': forms.Textarea(attrs={'placeholder': ('Опишите ваш заказ')}),
        }
        labels = {
            'date':'',
            'fio':'',
            'slug':'',
            'tel':'',
            'email':'',
            'insta':'',
            'fb':'',
            # 'face':'',
            # 'full_photo':'',
            # 'sex':'',
            # 'birthday':'',
            'lenth':'',
            'weight':'',
            'chest':'',
            'waist':'',
            'hips':'',
            'footwear':'',
            # 'hair_color':'',
            # 'haer_lenth':'',
            'money':'',
        }

        # , label = '', empty_label = _("Выбирите услугу")