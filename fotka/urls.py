from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from photo import views

from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns

from django.contrib.sitemaps.views import sitemap
from photo.sitemaps import PostSitemap, CaseSitemaps

sitemaps = {
    'posts': PostSitemap,
    'cases': CaseSitemaps,
}



urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    path('auth/', include('djoser.urls.jwt')),
    path('home-buh/', include('home_buh.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls'), name='accounts.'),
    path('clients/', include('clients.urls')),
    path('modeles/', include('modeles.urls')),
    # path('home-buh/', include('home_buh.urls')),
    path('720p/',  include('studio_buh.urls')),
    path('', include('photo.urls'), name='main'),
    path('photo/', views.Photo, name='photo'),
    path('video/', views.Video,  name='video'),
    path('aero/', views.Aero, name='aero'),
    path('contact/', views.ContactS, name='contact'),
    path('thanks/', TemplateView.as_view(template_name='static/thanks.html'), name='thanks'),

)
