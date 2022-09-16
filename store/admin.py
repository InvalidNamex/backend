from django.contrib import admin
from store.featureModel import ProcessorFeatures
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from store.inlines import *
from .models import *

@admin.register(Collections)
class CollectionsAdmin(admin.ModelAdmin):
    list_display = ['collectionName', 'collectionImage']

@admin.register(SubCollections)
class SubCollectionsAdmin(admin.ModelAdmin):
    list_display = ['subCollectionName', 'subcollectionImage']

@admin.register(Brands)
class BrandsAdmin(admin.ModelAdmin):
    list_display = ['brandName', 'brandImage']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['productName', 'productPrice', 'productAvailability', 'productSubCollection']
    list_editable = ['productPrice', 'productAvailability']
    list_per_page: int = 10
    inlines = [MonitorInline, ProcessorsInline, MotherBoardInline, RamInline, PowerSupplyInline, GraphicsCardInline, CoolingInline, CaseInline, StorageInline, NotebookInline, ProductImagesInline]
    list_select_related = ['productSubCollection']
    
@admin.register(Banners)
class BannersAdmin(admin.ModelAdmin):
    list_display = ['bannerProduct', 'bannerImage']
    search_fields = ['bannerProduct']

@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['promotionName', 'promotionDescription', 'promotionDiscount', 'promotionIsPercentage', 'promotionIsActive']
    search_fields = ['promotionName']

@admin.register(Customers)
class CustomersAdmin(BaseUserAdmin):
    pass

@admin.register(FeaturedProducts)
class FeaturedProductsAdmin(admin.ModelAdmin):
    list_display = ['featuredProduct']
