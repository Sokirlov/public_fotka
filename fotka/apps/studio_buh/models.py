from django.db import models
import django_filters

class Services(models.Model):
    name = models.CharField('Название услуги', max_length=300)
    price = models.DecimalField('Цена услуги', max_digits=6, decimal_places=2)
    idSort = models.PositiveSmallIntegerField('сортировка', default=99)

    class Meta:
        ordering = ['idSort']
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

class ClientSource(models.Model):
    name = models.CharField('Источник клиента', max_length=200)

    class Meta:
        ordering = ['id']
        verbose_name = 'Источник клиента'
        verbose_name_plural = 'Источники клиентов'

    def __str__(self):
        return self.name

class Clients(models.Model):
    date = models.DateTimeField('Дата регистрации', auto_now_add=True, null=True, blank=True)
    name = models.CharField('Имя клиента', max_length=300,  default='')
    email = models.EmailField('Емеил', blank=True, null=True)
    tel = models.CharField('Контактный телефон', max_length=22, unique=True)
    comments = models.CharField('Комментарии о клиенте', max_length=1000, blank=True, null=True)
    sourceClient = models.ForeignKey(ClientSource, on_delete=models.CASCADE, verbose_name='Откуда клеинта\nузнал о нас?', blank=True, null=True)

    class Meta:
        ordering = ['-id']
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        name_tel = self.tel + '\n\n ' + self.name
        return name_tel

class Administrators(models.Model):
    name = models.CharField('ФИО', max_length=200, )
    email = models.EmailField('e-mail', max_length=100, default='@gmail.com')
    tel = models.CharField('Контактный телефон', max_length=10, unique=True)
    viber = models.CharField('Viber', max_length=10, unique=True, null=True, blank=True)
    telegram = models.CharField('Telegram', max_length=10, unique=True, null=True, blank=True)
    whatsapp = models.CharField('WhatsApp', max_length=10, unique=True, null=True, blank=True)
    site = models.URLField('Ссылка на сайт', max_length=255, blank=True, null=True)
    fb = models.URLField('Ссылка на фейсбук', max_length=255, blank=True, null=True)
    insta = models.URLField('Ссылка на инстаграм', max_length=255, blank=True, null=True)
    cardNumber = models.CharField('Номер карты', max_length=16, blank=True, null=True)
    idSort = models.PositiveSmallIntegerField('Сорт', default=99)

    class Meta:
        ordering = ['idSort']
        verbose_name = 'Администратор'
        verbose_name_plural = 'Администраторы'

    def __str__(self):
        return self.name



class Income(models.Model):
    PAY_TYPE_CHOIS = (
        ('cash', 'Наличка'),
        ('card', 'Карточка'),
    )
    date_create_order = models.DateField('Дата заявки', auto_now_add=True, null=True, blank=True)
    tel = models.ForeignKey(Clients, on_delete=models.CASCADE, verbose_name='Тел. клеинта')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name='Услуга', default=' ', blank=True, null=True)
    date_ordering = models.DateTimeField('Дата аренды')
    order = models.PositiveSmallIntegerField('Сколько\nчасов',  default='0')
    who_admin = models.ForeignKey(Administrators, on_delete=models.CASCADE, verbose_name='Администратор', blank=True, null=True)
    prepay = models.FloatField('Предоплата', default='100', null=True, blank=True)
    payment = models.FloatField('Расчет', default='0', null=True, blank=True)
    payment_type = models.CharField('Метод оплаты', choices=PAY_TYPE_CHOIS, max_length=6, blank=True, null=True)
    comments = models.CharField('Коментарий к платежу', max_length=500, blank=True, null=True)
    fineshed = models.BooleanField('Закрыть заказ',  default='False')

    class Meta:
        ordering = ['-date_create_order']
        verbose_name = 'Доход'
        verbose_name_plural = 'Доходы'

    def __str__(self):
        return str(self.date_ordering)


class PaymentsCategory(models.Model):
    category = models.CharField('Имя категори расходов', max_length=50, default='')
    class Meta:
        verbose_name = 'Категория расходов'
        verbose_name_plural = 'Категория расходов'
    def __str__(self):
        return self.category

class Payments(models.Model):
    WHO_IS_PAY = (
        ('sokirlov', 'Кирилл'),
        ('alex_dun', 'Алекс'),
        ('studio', 'Студия наличка'),
        ('studio_card', 'Студия карта'),
    )
    date_create_payment = models.DateField('Дата заявки', auto_now_add=True, null=True, blank=True)
    payer = models.CharField('Кто оплатил', choices=WHO_IS_PAY, max_length=20)
    pay_name = models.CharField('Название\n(описание операции)', max_length=500, default='')
    payment = models.FloatField('Сумма платежа', help_text='Введите число, разделитель . \nПРИМЕР: ХХ.хх')
    category = models.ForeignKey(PaymentsCategory, on_delete=models.CASCADE, default='', blank=True)

    class Meta:
        ordering = ['-date_create_payment']
        verbose_name = 'Расходы'
        verbose_name_plural = 'Расходы'

    def __str__(self):
        return str(self.date_create_payment)

class PaymentsFilter(django_filters.FilterSet):
    category__category = django_filters.ModelChoiceFilter(field_name='category',
                                                          queryset=PaymentsCategory.objects.all(),)
    class Meta:
        model = Payments
        fields = {
            'date_create_payment': ['gte', 'lte'],
            'payer': ['exact'],
            'category__category': ['exact'],
        }

