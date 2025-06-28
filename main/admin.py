from django.contrib import admin
from .models import (
    Category, Product, Size, ProductGallery, Video, Color,
    HomepageBanner, EleganceSection, EleganceFeature, HeroSection, FlashSaleProduct
)

@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display = ('size',)
    search_fields = ('size',)

class ProductGalleryInline(admin.TabularInline):
    model = ProductGallery
    extra = 1

class ColorInline(admin.TabularInline):
    model = Color
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_featured')
    list_filter = ('is_featured', 'category')
    search_fields = ('name',)
    inlines = [ProductGalleryInline, ColorInline]
    filter_horizontal = ('sizes',) 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

@admin.register(FlashSaleProduct)
class FlashSaleProductAdmin(admin.ModelAdmin):
    list_display = ('product', 'discounted_price', 'sale_end_time')

# Register remaining models
admin.site.register(Video)
admin.site.register(Color)
admin.site.register(ProductGallery)
admin.site.register(HomepageBanner)
admin.site.register(EleganceSection)
admin.site.register(EleganceFeature)
admin.site.register(HeroSection)
