from django import template
from studio_buh.models import PaymentsCategory
register = template.Library()

@register.filter
def summvalios(value, arg):
    if value == None:
        value = 0
    if arg == None:
        arg = 0
    return value + arg

@register.filter
def replacekomatodot(value):
    return str(round(value, 0)).replace(',', '.')

@register.filter
def sokirlov_sum(val, obj):
    all = val.filter(payer=obj)
    arr = []
    for j in all:
        arr.append(j.payment)
    itog = sum(arr)
    return str(itog).replace(',', '.')

@register.filter
def intToWeekDay(numDay):
    if numDay == 1:
        return 'Понедельник'
    elif numDay == 2:
        return 'Вторник'
    elif numDay == 3:
        return 'Среда'
    elif numDay == 4:
        return 'Четверг'
    elif numDay == 5:
        return 'Пятница'
    elif numDay == 6:
        return 'Суббота'
    elif numDay == 7:
        return 'Воскресенье'
    else:
        return ' -- '

@register.filter
def idToCategory(numb):
    return PaymentsCategory.objects.get(id=numb)