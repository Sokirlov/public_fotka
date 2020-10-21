from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from photo import views

# from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    # path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    # path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('clients/', include('clients.urls')),
    path('modeles/', include('modeles.urls')),
    path('', include('photo.urls'), name='main'),
    path('photo/', views.Photo, name='photo'),
    path('video/', views.Video,  name='video'),
    path('aero/', views.Aero, name='aero'),
    path('contact/', views.ContactS, name='contact'),
    path('thanks/', TemplateView.as_view(template_name='static/thanks.html'), name='thanks'),
)


