from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    OPERATION_TYPS = (
        ('out', 'Расходы'),
        ('in', 'Доходы'),

    )
    categoryName = models.CharField('Категория операции', max_length=255, default='')
    operations = models.CharField('Тип операции', choices=OPERATION_TYPS, max_length=10)

    class Meta:
        verbose_name = 'Категория операции'
        verbose_name_plural = 'Категории операций'

    def __str__(self):
        return self.categoryName

class Operations(models.Model):
    OPERATION_TYPS = (
        ('out', 'Расходы'),
        ('in', 'Доходы'),
    )
    opertime = models.DateField('Дата операции', auto_now=False)
    operations = models.CharField('Тип операции', choices=OPERATION_TYPS, max_length=10)
    categoryId = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='categoryId')
    name = models.CharField('Название операции', max_length=255, blank=True, null=True)
    summa = models.IntegerField('Сумма операции')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['opertime']
        verbose_name = 'Операции'
        verbose_name_plural = 'Операций'

    def __str__(self):
        return self.name

class userProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    description=models.TextField(blank=True,null=True)
    location=models.CharField(max_length=30,blank=True)
    date_joined=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username