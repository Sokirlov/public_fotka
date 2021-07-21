from django.urls import path
from . import views

app_name = 'modeles'

urlpatterns =(
    path('', views.ModelesView, name='modele'),
    path('alls/', views.ModelesAllView, name='modeles_list'),
    path('all/', views.ModelesAllFreeView, name='modeles_list_free'),
)