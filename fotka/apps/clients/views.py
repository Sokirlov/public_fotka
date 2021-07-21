from django.views.generic import CreateView
from .models import Zakaz
from .forms import ZakazForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, render
from photo.models import Price


class ZakazView(CreateView):
    model = Zakaz
    form_class = ZakazForm
    success_url = reverse_lazy('thanks')

def index(request):
    if request.POST:
        form = ZakazView(request.POST)
        linkId = form.pagelink
        form.pagelink = Price.object.get(id=linkId)
        if form.is_valid():

            form.save()  # use form to save it in DB
            return render(request, 'index.html' )
    context = {'pagelink': pagelink, 'zakaz_form':form}

    return render(request, 'photo/category_detail.html', context)

