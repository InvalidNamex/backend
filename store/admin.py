from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.inlines import *
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'afterPrice', 'isDiscount', 'isNew', 'slug', 'availability', 'description', 'sku', 'category', 'subCategory', 'brand', 'model', 'lastUpdate', 'rating']
    list_editable = ['price', 'availability', 'afterPrice', 'isDiscount', 'isNew']
    list_per_page: int = 10
    inlines = [MonitorInline, ProcessorsInline, MotherBoardInline, RamInline, PowerSupplyInline, GraphicsCardInline, CoolingInline, CaseInline, StorageInline, NotebookInline, ProductImagesInline]
    list_select_related = ['subCategory']
    search_fields = ['name']
    
@admin.register(Promotion)
class PromotionAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'discount', 'isPercentage', 'isActive']
    search_fields = ['name']

@admin.register(Customer)
class CustomerAdmin(BaseUserAdmin):
    pass

@admin.register(FeaturedProduct)
class FeaturedProductAdmin(admin.ModelAdmin):
    list_display = ['product']
    search_fields = ['product']

@admin.register(ProductBanner)
class ProductBannerAdmin(admin.ModelAdmin):
    list_display = ['product', 'image']
    search_fields = ['product']

@admin.register(ImageBanner)
class ImageBannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    search_fields = ['name']

@admin.register(AdBanner)
class AdBannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'url']
    search_fields = ['name']

@admin.register(VideoBanner)
class VideoBannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'url']
    search_fields = ['name']

@admin.register(BrandBanner)
class BrandBannerAdmin(admin.ModelAdmin):
    list_display = ['name', 'brand', 'image']
    search_fields = ['name']
