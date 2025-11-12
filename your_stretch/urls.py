from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from debug_toolbar.toolbar import debug_toolbar_urls
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap
from core.views import (
    LandingView, 
    )
sitemaps = {
    'static': StaticViewSitemap,
}
urlpatterns = [
    path('z3rxp8hLmkJqXvBw/', admin.site.urls),
    path('', LandingView.as_view(), name='landing'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
] + debug_toolbar_urls()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)