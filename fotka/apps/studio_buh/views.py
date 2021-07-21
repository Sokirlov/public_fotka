from django.shortcuts import render
from datetime import timedelta, date
import datetime
from .models import Income, Payments, Clients, PaymentsFilter, PaymentsCategory, Administrators
from .forms import IncomeForm, PaymentsForm, ClientsForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.contrib import messages
from .calendar import creat_event_call

today = datetime.date.today()

def sumObjects(forSum):
    try:
        ppay = sumPrepay(forSum)
    except:
        ppay = 0
    arr = []
    for i in forSum:
        arr.append(i.payment)
    return sum(arr) + ppay

def sumPrepay(forSum):
    arr = []
    for i in forSum:
        arr.append(i.prepay)
    return sum(arr)

def searchParsedArr(obj, parsPole):
    arr = []
    for i in obj.values():
        x = i['%s' % parsPole]
        try:
            arr.append(x.isoweekday())
        except:
            arr.append(x)
    z = set(arr)
    forSearch = list(z)
    forSearch.sort()
    return forSearch



def parseWeekDay(obj, serchArr):
    theDays = {}
    try:
        for i in serchArr:
            forOneDays = obj.filter(date_create_payment__week_day=i)
            theDays[i] = round(sumObjects(forOneDays), 2)
    except:
        for i in serchArr:
            forOneDays = obj.filter(date_ordering__week_day=i)
            theDays[i] = round(sumObjects(forOneDays), 2)
    return theDays

def parseCatOfPayments(obj, serchArr):
    catData = {}
    try:
        for i in serchArr:
            forOneDays = obj.filter(category_id=i)
            catData[i] = round(sumObjects(forOneDays), 2)
    except:
        pass
    return catData




def parseOfPeriods(obj):
    all_time_summ = round(sumObjects(obj), 2)
    try:
        this_year = obj.filter(date_ordering__year=today.year)
        this_month = this_year.filter(date_ordering__month=today.month)
        parsedOfWeekDay = parseWeekDay(this_year, searchParsedArr(this_year, 'date_ordering'))
    except:
        this_year = obj.filter(date_create_payment__year=today.year)
        this_month = this_year.filter(date_create_payment__month=today.month)
        parsedOfWeekDay = parseWeekDay(this_year, searchParsedArr(this_year, 'date_create_payment'))
    try:
        parsedCategory = parseCatOfPayments(this_year, searchParsedArr(this_year, 'category_id'))
        print('parsedCategory', parsedCategory)
    except:
        parsedCategory = None
        print('parsedCategory', parsedCategory)

    this_year_summ = round(sumObjects(this_year), 2)
    this_month_summ = round(sumObjects(this_month), 2)

    return {'all_time_summ': all_time_summ,
            'this_year_summ':this_year_summ,
            'this_month_summ':this_month_summ,
            'parsedOfWeekDay': parsedOfWeekDay,
            'parsedCategory': parsedCategory,}



@permission_required('studio_buh.view_payments')
def studio_buh_main_view(request):
    incoms_all = Income.objects.filter(fineshed=True)
    incoms = parseOfPeriods(incoms_all)
    payments_all = Payments.objects.all()
    payments = parseOfPeriods(payments_all)

    return render(request, '720p/index.html',
                  {'incoms_all': incoms_all,
                   'incoms': incoms,
                   'payments_all': payments_all,
                   'payments': payments})


@permission_required('studio_buh.view_payments')
def all_payments(request):
    submitted = False
    if request.POST:
        form = PaymentsForm(request.POST)
        if form.is_valid():
            date_create_order: date = datetime.date.today()
            form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            form = PaymentsForm(request.POST)
    else:
        form = PaymentsForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    this_month = str(today.year)+'-'+str(today.month)+'-01'
    payments = PaymentsFilter(request.GET, queryset=Payments.objects.all().order_by('-date_create_payment'))
    alexdun_all = Payments.objects.filter(payer='alex_dun')
    alexdun_arr = []
    for j in alexdun_all:
        alexdun_arr.append(j.payment)
    alexdun = sum(alexdun_arr)
    sokirlov_all = Payments.objects.filter(payer='sokirlov')
    sokirlov_arr = []
    for j in sokirlov_all:
        sokirlov_arr.append(j.payment)
    sokirlov = sum(sokirlov_arr)
    return render(request, '720p/payments.html', {'form': form, 'payments': payments,
                                                  'alexdun': alexdun, 'sokirlov': sokirlov,
                                                  'submitted': submitted})

def future_incoms(request):
    submitted = False
    if request.POST:
        form = IncomeForm(request.POST)
        if form.is_valid():
            date_create_order = datetime.date.today()
            new_order_info = form.cleaned_data

            if str(new_order_info['service']) == 'Аренда Циклорамы' \
                    or str(new_order_info['service']) == 'Аренда Темного зала':
                creat_event_call(new_order_info)
            form.save()
            return HttpResponseRedirect('?submitted=True')
        else:
            form = IncomeForm(request.POST)
            messages.error(request, "Error")
    else:
        form = IncomeForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    period = today - timedelta(days=10)
    incoms = Income.objects.filter(fineshed=False).order_by('-date_ordering')
    return render(request, '720p/orders.html', {'incoms': incoms,
                                                'title': 'Заказы',
                                                'form': form,
                                                'submitted': submitted})



@permission_required('studio_buh.view_income')
def last_incoms(request):
    incoms = Income.objects.filter(fineshed=True).order_by('-date_ordering')
    prepays = Income.objects.filter(prepay__gt=0).order_by('-date_ordering')
    incoms_cash = Income.objects.filter(fineshed=True, payment_type='cash')
    incoms_card = Income.objects.filter(fineshed=True, payment_type='card')
    studio_payments_cash = Payments.objects.filter(payer='studio')
    studio_payments_card = Payments.objects.filter(payer='studio_card')
    summ_studio_payments_cash = sumObjects(studio_payments_cash)
    summ_studio_payments_card =sumObjects(studio_payments_card)

    prepay_arr = []
    for i in prepays:
        prepay_arr.append(i.prepay)
    sum_prepay = sum(prepay_arr)
    sum_cash = sumObjects(incoms_cash)
    sum_card = sumObjects(incoms_card)+sum_prepay
    sum_studio = sum_cash + sum_card
    balance_cash = round(sumObjects(incoms_cash) - summ_studio_payments_cash, 2)
    balance_card = round(sumObjects(incoms_card) + sum_prepay - summ_studio_payments_card, 2)
    balance_sum = balance_card + balance_cash

    return render(request, '720p/profit.html', {'incoms': incoms,
                                                'title': 'Прибыль',
                                                'sum_studio': sum_studio,
                                                'sum_cash': sum_cash,
                                                'sum_card': sum_card,
                                                'balance_sum': balance_sum,
                                                'balance_cash': balance_cash,
                                                'balance_card': balance_card,})


class Future_incomsUpdate(UpdateView):
    model = Income
    fields = '__all__'
    success_url = '/uk/720p/'
    template_name = '720p/income_form.html'

class ClientsCreate(CreateView):
    model = Clients
    template_name = '720p/create_client.html'
    from_class = 'clients_add'
    fields = '__all__'

class ClientsUpdate(UpdateView):
    model = Clients
    template_name = '720p/clients_update_form.html'
    from_class = 'clients_add'
    fields = '__all__'
    success_url = '/720p/clients/'

class ClientsDelete(DeleteView):
    model = Clients
    success_url = reverse_lazy('client-list')

def clients_all_add(request):

    submitted = False
    if request.POST:
        form = ClientsForm(request.POST)
        if form.is_valid():
            date_create_order = datetime.date.today()
            form.save()
            cd = form.cleaned_data
            submitted = True
            return HttpResponseRedirect('/720p/clients?submitted=True')
        else:
            messages.error(request, "Такой клиент уже есть")
    else:
        form = ClientsForm(request.POST)
        if 'submitted' in request.GET:
            submitted = True
    clients = Clients.objects.all().prefetch_related('income_set')
    print(clients)
    return render(request, '720p/clients_llist.html', {'object_list': clients,
                                                       'form': form,
                                                       'submitted': submitted})