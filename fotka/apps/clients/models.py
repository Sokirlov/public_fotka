from django.db import models
from django.urls import reverse

class Zakaz(models.Model):
    STATUS_CHOICES = (
        ('new', 'Новый Заказы'),
        ('in_progres', 'В процессе'),
        ('finished', 'Закончено'),
    )
    name = models.CharField(max_length=25)
    email = models.EmailField()
    tel = models.CharField(max_length=10)
    zakazTime = models.DateTimeField(auto_now_add=True)
    comments = models.CharField(max_length=200, blank=True)
    pagelink = models.CharField(max_length=200, blank=True, )
    status = models.CharField('Состояние', max_length=10, choices=STATUS_CHOICES, default='new')

    # def get_absolute_url(self):
    #     return reverse('contact',) # kwargs = {'razdel': self.razdel, 'slug': self.slug})
    class Meta:
        verbose_name_plural = 'Заявки'
    def __str__(self):
        return self.name