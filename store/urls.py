from django.urls import path
from . import views

# URLConf
urlpatterns = [
    path('collections/', views.collection_list),
    path('sub-collection/<int:id>/', views.subCollection_list),
    path('product/<int:id>/', views.product_details),
    path('featured-list/', views.featured_list),
]
