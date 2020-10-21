from django import template
register = template.Library()
from photo.models import Category, CaseWork, Globals
from django.utils.safestring import mark_safe
# from .models import Category, CaseWork
import markdown


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(text)

@register.filter(name='preview')
def cut_arrey(self):
    return self[0].Gallery

@register.filter(name='bdcb')
def bredcrumbs(path):
    a = path.split('/')
    a.pop()
    arurl = ''
    ar = ''
    str = ''
    def parsing(x):
        dict = {'ru': 'Главная', 'uk':'Головна', 'en':'Home',}
        try:
            categ = Category.objects.get(slug=x)
        except:
            categ = None
        try:
            case = CaseWork.objects.get(link=x)
        except:
            case = None
        try:
            glob = Globals.objects.get(indexName=x)
        except:
            glob = None

        if categ != None:
            return categ.categoryName
        elif case != None:
            return case.title
        elif glob != None:
            return glob.GlobalName
        elif dict.get(x):
            return dict[x]
        else:
                return x

    for i in a:
        ar += i + '/'
        idn = parsing(i)
        arurl = "<a href=\"" + ar + "\">" + idn + "</a>"
        str += ' » &nbsp;' + arurl
    return str[2:]

@register.filter(name='socials')
def bredcrumbs(link):
    b = link.split('/')
    soc_link = '<a href="' + link + '">' + b[-1] + '</a>'
    return soc_link

# @register.filter(name='globals')
# def globals(gl):
#     glob = Globals.objects.get(indexName=gl)
#     return glob.GlobalName

@register.filter(name='videobanner')
def bannervideo(video):
    b = video.split('com/')
    link = b[0] + 'com/embed/' + b[1] + '&autoplay=1&controls=0&loop=1&start=0&color=white&iv_load_policy=3'
    return link

@register.filter(name='youtube')
def youtube(link):
    arr = link.split('/')
    goodlink = 'https://www.youtube.com/embed/' + arr[-1]
    return goodlink