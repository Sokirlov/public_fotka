from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required
from . import views
from .views import *


app_name = 'studio_buh'

urlpatterns =(
    path('statistic/', login_required(views.studio_buh_main_view), name='statistic'),
    path('payments/', login_required(views.all_payments), name='payments'),
    path('', login_required(views.future_incoms), name='future_incoms'),
    path('last-orders/', login_required(views.last_incoms), name='last_incoms'),
    path('future-order/<pk>/upd/', views.Future_incomsUpdate.as_view(), name='order_update'),
    path('clients/', login_required(views.clients_all_add), name='client_list'),
    path('clients/add/', ClientsCreate.as_view(), name='client_add'),
    re_path(r'clients/(?P<pk>\d+)/upd$', ClientsUpdate.as_view(), name='client_update'),
    re_path(r'clients/(?P<pk>\d+)/delete/$', ClientsDelete.as_view(), name='client_delete'),
)




