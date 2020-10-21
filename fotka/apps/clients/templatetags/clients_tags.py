from django import template
from clients.forms import ZakazForm

register = template.Library()

@register.inclusion_tag('clients/form.html')
def zakaz_form():

    return {'zakaz_form': ZakazForm()}