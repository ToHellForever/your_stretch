# core/sitemaps.py

from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from core.models import Product, Profile

class StaticViewSitemap(Sitemap):
    priority = 1.0
    changefreq = "daily"

    def items(self):
        return ['landing']

    def location(self, item):
        return reverse(item)

class ProductSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('product_detail', kwargs={'pk': obj.pk})

class ProfileSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.8

    def items(self):
        return Profile.objects.all()

    def location(self, obj):
        return reverse('profile_detail', kwargs={'pk': obj.pk})
