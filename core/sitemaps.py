# core/sitemaps.py

from django.contrib.sitemaps import Sitemap
from .models import Product, Profile

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.7

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return f'/product/{obj.pk}/'

class ProfileSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.6

    def items(self):
        return Profile.objects.all()

    def location(self, obj):
        return f'/profile/{obj.pk}/'

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "yearly"

    def items(self):
        return ['landing']

    def location(self, item):
        return reverse(item)