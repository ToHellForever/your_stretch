from django.contrib import admin
from .models import Product, Profile, Gallery, GalleryImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price')
    list_filter = ('price',)
    search_fields = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'area', 'angles', 'profile', 'price')
    list_filter = ('profile', 'price')
    search_fields = ('name', 'profile')

class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1

@admin.register(Gallery)
class GalleryAdmin(admin.ModelAdmin):
    inlines = [GalleryImageInline]
    list_display = ('id', 'name')
    search_fields = ('name',)
