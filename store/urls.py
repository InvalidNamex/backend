from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('categories/', views.category_list),
    path('sub-categories/<int:id>/', views.subCategory_list),
    path('product/<int:id>/', views.product_details),
    path('featured-list/', views.featured_list),
    path('brand-list/', views.brand_list),
    path('product-banner-list/', views.product_banner_list),
    path('image-banner-list/', views.image_banner_list),
    path('ads-banner-list/', views.ads_banner_list),
    path('video-banner-list/', views.video_banner_list),
    path('subCategory-products-list/<int:id>/', views.subCategory_products_list),
    path('brand-products-list/<int:id>/', views.brand_products_list),
    path('brand-banner-list/<int:id>/', views.brand_banner_list),
    path('new-products-list/', views.new_products_list),
    path('hot-products-list/', views.hot_products_list),
]
