from django import template
from clients.forms import ZakazForm

register = template.Library()

@register.inclusion_tag('clients/form.html', takes_context=True)
def zakaz_form(context):
    # context =
    #     for i in args.request.path:
    return {'zakaz_form': ZakazForm(context)}