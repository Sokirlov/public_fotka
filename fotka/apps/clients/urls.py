from django.urls import path
from .views import ZakazView

app_name = 'clients'

urlpatterns =[
    path('', ZakazView.as_view(), name='zakaz')
]