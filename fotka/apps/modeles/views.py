from .models import Modeles, ModelesFilter
from .forms import ModelesForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .filters import ModelesAllViewFilter



def ModelesView(request):
    if request.method == 'POST':
        modelesFormdon = ModelesForm(request.POST, request.FILES)
        if modelesFormdon.is_valid():
            modelesFormdon.save()
            return HttpResponseRedirect('/thanks/')
        else:
            modeles_form = modelesFormdon
    else:
        modeles_form = ModelesForm()
    return render(request, 'modeles/modeles_form.html', {'modeles_form': modeles_form})


@login_required()
def ModelesAllView(request):
    # modelesalllist = Modeles.objects.all()
    modelesalllist = ModelesFilter(request.GET, queryset=Modeles.objects.all().order_by('id'))
    return render(request, 'modeles/modelesall_detail.html', {'modeles_all_list': modelesalllist})
