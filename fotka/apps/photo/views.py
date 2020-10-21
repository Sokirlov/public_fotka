from django.shortcuts import render
from django.views.generic.list import ListView
from django.http import Http404, HttpResponseRedirect
from django.views.generic.detail import DetailView
from .models import Category, Gallery, Videopholio, Advantages, Price, CaseWork, Contacts, CaseGallery


def category(request):
    categorys = Category.objects.filter(status='published').order_by('idsort')
    return render(request, 'photo/category.html', {'categorys': categorys})


def razdel(request):
    categorys = Category.objects.filter(status='published').order_by('idsort')
    return render(request, 'photo/category.html', {'categorys': categorys})


class CategoryDetailView(DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(CategoryDetailView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        zp = self
        context['gallery'] = Gallery.objects.filter(slug=zp.get_object())
        context['videopholio'] = Videopholio.objects.filter(slug=zp.get_object()).order_by('idsort')
        context['advantages'] = Advantages.objects.filter(slug=zp.get_object(), status='published').order_by('idsort')
        context['prices'] = Price.objects.filter(slug=zp.get_object(), status='published').order_by('idsort')
        context['case'] = CaseWork.objects.filter(slug=zp.get_object(), status='published').order_by(
            'idsort').prefetch_related('casegallery_set')

        return context


class CaseWorkDetailView(DetailView):
    model = CaseWork
    slug_field = 'link'
    context_object_name = 'case'

    def get_object(self, queryset=None):
        queryset = CaseWork.objects.filter(slug__slug=self.kwargs['slug'], link=self.kwargs['link']).prefetch_related(
            'casegallery_set').order_by('idsort')
        return queryset


def Aero(request):
    categorys = Category.objects.filter(status='published', razdel='aero').order_by('idsort')
    return render(request, 'photo/category.html', {'categorys': categorys})


def Video(request):
    categorys = Category.objects.filter(status='published', razdel='video').order_by('idsort')
    return render(request, 'photo/category.html', {'categorys': categorys})


def Photo(request):
    categorys = Category.objects.filter(status='published', razdel='photo').order_by('idsort')
    return render(request, 'photo/category.html', {'categorys': categorys})


def ContactS(request):
    contacts = Contacts.objects.filter(status='published', ).order_by('idsort')
    return render(request, 'photo/contacts.html', {'contacts': contacts})
