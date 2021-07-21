from django.contrib.sitemaps import Sitemap
from .models import Category, CaseWork

class PostSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9
    i18n = True

    def items(self):
        return Category.objects.filter(status='published')

class CaseSitemaps(Sitemap):
    hangefreq = 'monthly'
    priority = 0.6
    i18n = True

    def items(self):
        return CaseWork.objects.filter(status='published')