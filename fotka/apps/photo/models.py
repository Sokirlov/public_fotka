from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from io import BytesIO
from PIL import Image
from django.core.files import File


def compress(image):
    im = Image.open(image)
    im_io = BytesIO()
    im.save(im_io, 'JPEG', quality=60)
    new_image = File(im_io, name=image.name)
    return new_image

def dublicateDelite(image):
    arr2 = []
    for a in image.split('/'):
        if (arr2.count(a) == 0):
            arr2.append(a)
    newUrls = '/'.join(arr2)
    return newUrls

def newPath(imgPath, image):
    containPath = image.find(imgPath)

    if (containPath >0):
        return image
    else:
        return imgPath + image

def bannerImg(obj, image):
    return  'photo/' + str(obj.slug) +'/banner.jpg'

def gallPath(obj, image):
    imgPath = 'photo/' + str(obj.slug.slug) + '/gallery/'
    dublicateDelite(image)
    return newPath(imgPath, image)


def advanImg(obj, image):
    imgPath = 'photo/' + str(obj.slug.slug) + '/advantages/'
    dublicateDelite(image)
    return newPath(imgPath, image)

def caseImg(obj, image):
    imgPath = 'photo/' + str(obj.link.slug.slug) + '/csae/' + str(obj.link.link) +'/'
    dublicateDelite(image)
    return newPath(imgPath, image)

def blogImg(obj, image):
    imgPath = 'photo/' + str(obj.slug.slug) + '/blog/' + str(obj.link) +'/'
    dublicateDelite(image)
    return newPath(imgPath, image)

class Category(models.Model):
    RAZDEL_CHOUICES = (
        ('photo', 'Фотосъемка'),
        ('video', 'Видеосъемка'),
        ('aero', 'Аэросъемка'),
    )
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    def get_absolute_url(self):
        return reverse('photo:detail', kwargs = {'razdel': self.razdel, 'slug': self.slug,}) ## args=[str(self.slug)])

    razdel = models.CharField('Категория', max_length= 10, choices=RAZDEL_CHOUICES, null=True)
    categoryName = models.CharField('Название страницы', max_length=200)
    slug = models.SlugField('URL-адрес', help_text='Адрес для страницы', db_index=True, unique=True,)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    status = models.CharField('Состояние', max_length=10, choices=STATUS_CHOICES, default='draft')
    keyWords = models.CharField('Keywords', help_text='Ключевые слова для поисковиков', max_length=200, blank=True)
    descriptions = models.CharField('Descriptions', help_text='Описание для поисковиков', max_length=300, blank=True)
    categoryBanner = models.ImageField('Баннер', upload_to=bannerImg, blank=True, max_length=500)
    video = models.CharField(max_length=200, blank=True)
    introText = HTMLField('Вступительный текст', blank=True)

    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.categoryBanner))

    image_tag.short_description = 'Баннер'
                       
    class Meta:
        ordering = ['idsort']
        verbose_name = 'Услуга'
        verbose_name_plural = '1 Услуги'

    def __str__(self):
        return self.categoryName

class Gallery(models.Model):
    slug = models.ForeignKey(Category,  on_delete=models.CASCADE)
    imgTitle = models.CharField('Заголовк фото', max_length=200)
    categoryGallery = models.ImageField('Выберет фото', upload_to=gallPath, blank=True, max_length=500)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)

    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.categoryGallery))

    image_tag.short_description = 'categoryGallery'

    def save(self, *args, **kwargs):
        try:
            new_image = compress(self.categoryGallery)
            self.categoryGallery = new_image
        except ValueError:
            pass
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return self.imgTitle

class Advantages(models.Model):
    POSITION_CHOICES = (
        ('left', 'Слева'),
        ('center', 'В центре'),
        ('right', 'Справа'),
    )
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    slug = models.ForeignKey(Category,  on_delete=models.CASCADE)
    advantagesTitle = models.CharField('Загаловок блока\nможно пропустить', max_length=100, blank=True)
    position = models.CharField('Выберете положение\nтекста', max_length=10, choices=POSITION_CHOICES, default='left')
    status = models.CharField('Включить/спрятать', max_length=10, choices=STATUS_CHOICES, default='draft')
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    advantagesImage = models.ImageField('Выберет фото\nдля блока', upload_to=advanImg, blank=True, null=True, max_length=500)
    advantagesText = HTMLField('Текст блока\nприемущества', blank=True, null=True)

    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.advantagesImage))

    image_tag.short_description = 'Фото'

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = 'Приемущества:'

    def __str__(self):
        return self.advantagesTitle

class Price(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    slug = models.ForeignKey(Category,  on_delete=models.CASCADE)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    status = models.CharField('Состояние', max_length=10, choices=STATUS_CHOICES, default='draft')
    priceBlockName = models.CharField('Название блока', max_length=100, blank=True, null=True)
    priceBlockText = HTMLField('Условия блока\nцены', max_length=1000, blank=True, null=True)
    priceBlockCount = models.PositiveSmallIntegerField('Цена пакета', blank=True, null=True)

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = 'Цены'

    def __str__(self):
        return self.priceBlockName



class CaseWork(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )

    slug = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    link = models.SlugField('link', db_index=True, unique=True)
    status = models.CharField('Состояние', max_length=10,  choices=STATUS_CHOICES, default='draft')
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    title = models.CharField('Название', unique=True, max_length=200)
    keyWords = models.CharField('Keywords', help_text='Ключевые слова для поисковиков', max_length=200, blank=True)
    descriptions = models.CharField('Descriptions', help_text='Описание для поисковиков', max_length=300, blank=True)
    text = HTMLField('Описание клиента\nили заказа', blank=True)
    bannerPositionX = models.SmallIntegerField('Сдвиг по ширине в \"VW\"', default=0)
    bannerPositionY = models.SmallIntegerField('Сдвиг по высоте в \"VH\"', default=0)
    bannerSize = models.SmallIntegerField('Размер фото в \"VW\"', default=50)

    def get_absolute_url(self):
        return reverse('photo:case', kwargs={
            'razdel': self.slug.razdel,
            'slug': self.slug.slug,
            'link': self.link,
        })

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Кейс работ'
        verbose_name_plural = '2 Кейс работ'

    def __str__(self):
        return self.link


class CaseGallery(models.Model):
    link = models.ForeignKey(CaseWork, max_length=200, default='', on_delete=models.CASCADE)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    imgAlt = models.CharField('Заголовок картинки', max_length=200, default='', blank=True)
    Gallery = models.ImageField('Выберет фото', upload_to=caseImg, blank=True, max_length=500)

    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.Gallery))

    image_tag.short_description = 'Gallery'

    def save(self, *args, **kwargs):
        try:
            new_image = compress(self.Gallery)
        except ValueError:
            new_image = self.Gallery
        self.Gallery = new_image
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = 'Кейс работ фото'

    def __str__(self):
        return self.imgAlt



class Contacts(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )
    name = models.CharField('ФИО', max_length=70)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    status = models.CharField('Состояние', max_length=10,  choices=STATUS_CHOICES, default='draft')
    photo = models.ImageField('Выберет фото', upload_to='photographers/', blank=True, max_length=500)
    tel = models.CharField('Телефон с 0хх', max_length=10, blank=True)
    fb = models.CharField('Ссылка на Facebook', max_length=99, blank=True)
    insta = models.CharField('Ссылка на Instagram', max_length=99, blank=True)
    about = HTMLField('Описание фотографа\nопыт работы,\n\nсколько лет на рынке', blank=True)

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = '9 Контакты'

    def __str__(self):
        return self.name

class Videopholio(models.Model):
    slug = models.ForeignKey(Category,  on_delete=models.CASCADE)
    videoTitle = models.CharField('Заголовк видео', max_length=200)
    videoLink = models.CharField('Укажите линк на видео', max_length=200)
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)

    class Meta:
        ordering = ['idsort']
        verbose_name = '  —'
        verbose_name_plural = 'Видео'

    def __str__(self):
        return self.videoTitle

class BlogPhoto(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Отключено'),
        ('published', 'Включено'),
    )

    slug = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
    link= models.SlugField('link', db_index=True, unique=True)
    status = models.CharField('Состояние', max_length=10,  choices=STATUS_CHOICES, default='draft')
    idsort = models.PositiveSmallIntegerField('Сортировка', null=True)
    title = models.CharField('Название', unique=True, max_length=200)
    keyWords = models.CharField('Keywords', help_text='Ключевые слова для поисковиков', max_length=200, blank=True)
    descriptions = models.CharField('Descriptions', help_text='Описание для поисковиков', max_length=300, blank=True)
    photo = models.ImageField('Выберет фото', upload_to=blogImg, blank=True, max_length=500)
    text = HTMLField('Описание клиента\nили заказа', blank=True)

    def get_absolute_url(self):
        return reverse('photo:blog', kwargs={
            'razdel': self.slug.razdel,
            'slug': self.slug.slug,
            'blog': 'blog',
            'link': self.link,
        })
    def image_tag(self):
        from django.utils.safestring import  mark_safe
        return mark_safe('<img src="/media/%s" width="150" />' % (self.photo))

    image_tag.short_description = 'photo_im'

    def save(self, *args, **kwargs):
        try:
            new_image = compress(self.photo)
        except ValueError:
            new_image = self.photo
        self.photo = new_image
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['idsort']
        verbose_name = 'Статья'
        verbose_name_plural = '4 Статьи'

    def __str__(self):
        return self.link