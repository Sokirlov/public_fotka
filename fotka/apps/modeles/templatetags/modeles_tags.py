from django import template
from modeles.forms import ModelesForm

register = template.Library()

@register.filter(name='instas')
def markdown_format(link):
    a = link.split('/')
    b = a[-1]
    c = b.replace('@', '')
    d = 'https://www.instagram.com/' + c
    return d

@register.filter(name='insta_name')
def markdown_format(link):
    a = link.split('/')
    b = a[-1]
    return b