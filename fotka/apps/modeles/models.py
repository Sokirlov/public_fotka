from django.db import models
from django.utils.crypto import get_random_string

def modelPhoto(obj, image):

    gen_img = get_random_string(length=20)
    return  'modeles/' + str(obj.sex) + '/'+ str(obj.lenth) +'/' + gen_img +'.jpg'

class Modeles(models.Model):
    SEX_CHOICES = (
        ('men', 'Мужской'),
        ('women', 'Женский'),
    )
    HAIR_COLOR = (
        ('Блонд', 'Блонд'),
        ('Шатен', 'Шатен'),
        ('Рыжий', 'Рыжий'),
        ('Брюне', 'Брюне'),
        ('другой', 'другой'),
    )
    HEAR_LENTH =(
        ('Нет волос', 'Нет волос'),
        ('Короткие', 'Короткие'),
        ('До плеч', 'До плеч'),
        ('До лопаток', 'До лопаток'),
        ('До пояса', 'До пояса'),
    )
    date = models.DateTimeField(auto_now_add=True)
    fio = models.CharField('Фамилия Имя Отчество', max_length= 200)
    tel = models.CharField('Номер телефона', max_length= 200)
    email = models.EmailField('Електронна адреса', max_length= 200)
    insta = models.CharField('Ссылка на инстаграм', max_length= 200)
    fb = models.CharField('Ссылка на Фейсбук', max_length= 200)
    face = models.ImageField('Фото Лица', upload_to=modelPhoto, blank=True, null=True)
    full_photo = models.ImageField('Фото в полный рост', upload_to=modelPhoto, blank=True, null=True)
    sex = models.CharField('Пол', max_length=10, choices=SEX_CHOICES)
    birthday = models.DateField('Дата рождения', auto_now=False, blank=True, null=True)
    lenth = models.PositiveSmallIntegerField('Рост СМ',)
    weight = models.PositiveSmallIntegerField('Вес в кг',)
    chest = models.PositiveSmallIntegerField('Обхват груди в см',)
    waist = models.PositiveSmallIntegerField('Обхват талии в см', )
    hips = models.PositiveSmallIntegerField('Обхват бедер в см', )
    footwear = models.PositiveSmallIntegerField('Размер обуви', )
    hair_color = models.CharField('Цвет волос', max_length=10, choices=HAIR_COLOR)
    haer_lenth = models.CharField('Длина волос', max_length=10, choices=HEAR_LENTH)
    money = models.PositiveSmallIntegerField('Гонорар за съемку в грн', )

    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.face))

    image_tag.short_description = 'Фото лица'

    class Meta:
        verbose_name_plural = 'Модели'
    def __str__(self):
        return self.email

import django_filters
class ModelesFilter(django_filters.FilterSet):
    # qrs = Modeles.objects.all().defer('lenth')
    # lenth = django_filters.filters.ModelMultipleChoiceFilter(
    #     field_name='lenth',
    #     to_field_name='lenth',
    #     queryset=qrs,
    # )

    class Meta:
        model = Modeles
        # fields = [ 'sex', 'birthday', 'lenth', 'weight', 'chest', 'waist', 'hips', 'footwear', 'hair_color', 'haer_lenth', 'money',]
        fields = {

            'sex': ['exact'],
            # 'birthday': ['gt', 'lt'],
            'lenth': ['gt', 'lt'],
            'weight': ['gt', 'lt'],
            'chest': ['gt', 'lt'],
            'waist': ['gt', 'lt'],
            'hips': ['gt', 'lt'],
            'footwear': ['gt', 'lt'],
            'hair_color': ['exact'],
            'haer_lenth': ['exact'],
            'money': ['gt', 'lt'],

        }