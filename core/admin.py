from django.contrib import admin
from decimal import InvalidOperation
from .models import Product, Profile, Gallery, GalleryImage, Banner, MobileBanner, Order, CallbackRequest

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

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id','image')
    
    
    
@admin.register(MobileBanner)
class MobileBannerAdmin(admin.ModelAdmin):
    list_display = ('id','image')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'safe_area', 'corners', 'lights', 'pipes', 'ceiling_type', 'phone', 'created_at')
    list_filter = ('ceiling_type', 'created_at')
    search_fields = ('phone', 'comment')

    def safe_area(self, obj):
        try:
            return obj.area
        except (ValueError, TypeError, InvalidOperation):
            return "Некорректное значение"
    safe_area.short_description = 'Площадь потолка (м²)'
    safe_area.admin_order_field = 'area'

@admin.register(CallbackRequest)
class CallbackRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'phone', 'created_at')
    search_fields = ('phone',)
