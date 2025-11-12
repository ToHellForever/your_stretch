# core/sitemaps.py

from django.contrib.sitemaps import Sitemap

class StaticViewSitemap(Sitemap):
    priority = 0.5
    changefreq = "yearly"

    def items(self):
        return ['landing']

    def location(self, item):
        return reverse(item)