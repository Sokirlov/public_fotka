# from django.conf.urls.i18n import i18n_patterns
from django.urls import path
from .views import CategoryDetailView, CaseWorkDetailView
from . import views


app_name = 'photo'

urlpatterns = [
	path('', views.razdel, name='main'),
	path('<slug:razdel>/<slug:slug>/<slug:link>/', CaseWorkDetailView.as_view(), name='case'),
	path('<slug:razdel>/<slug:slug>/', CategoryDetailView.as_view(), name='detail'),


]
