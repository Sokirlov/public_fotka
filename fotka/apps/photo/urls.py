from django.urls import path
from django.views.generic import TemplateView
from .views import CategoryDetailView, CaseWorkDetailView, BlogPhotoDetailView, BlogPhotoListView
from . import views


app_name = 'photo'

urlpatterns = [
	path('', views.razdel, name='main'),
	path('<slug:razdel>/<slug:slug>/<slug:link>/', CaseWorkDetailView.as_view(), name='case'),
	path('<slug:razdel>/<slug:slug>/<slug:blog>/', BlogPhotoListView.as_view(), name='blog-all'),
	path('<slug:razdel>/<slug:slug>/<slug:blog>/<slug:link>/', BlogPhotoDetailView.as_view(), name='blog'),
	path('policy-privacy', TemplateView.as_view(template_name='photo/privacy.html'), name='policy-privacy'),
	path('<slug:razdel>/<slug:slug>/', CategoryDetailView.as_view(), name='detail'),

]
