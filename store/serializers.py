from dataclasses import field
from rest_framework import serializers
from store.featureModel import *
from store.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = ['id', 'name', 'category', 'image']

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name', 'image']

class PromotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotion
        fields = ['id', 'name', 'description', 'discount', 'isPercentage', 'isActive' ]

class FeaturedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedProduct
        fields = ['id', 'product' , 'createdAt']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'afterPrice', 'isDiscount', 'isNew', 'slug', 'availability', 'description', 'sku', 'category', 'subCategory', 'brand', 'model', 'lastUpdate', 'rating', 'imageOne', 'imageTwo', 'imageThree', 'imageFour', 'imageFive', 'imageSix', 'imageSeven', 'imageEight', 'imageNine', 'imageTen']

# class CustomersSerializer(serializers.ModelSerializer):
#     model = Customer
#     fields = ['id', 'customerFirstName', 'customerLastName', 'customerEmail', 'customerPhone', 'customerCreationDate', 'customerIsVerified']

class AddressesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'customer','title', 'lineOne','lineTwo', 'description']

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = ['id', 'customer', 'products', 'likedDate']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'CreatedAt', 'cartCustomer']

class PurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseItem
        fields = ['id', 'cart', 'product', 'quantity', 'unitPrice']

class ProductsFeatures(serializers.ModelField):
    id = serializers.IntegerField()
    productPrice = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')
    def calc_tax(self, product:Product):
        return product.unit_price * 1.1

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorFeatures
        fields = ['displayRes', 'screenSize', 'panelType', 'responseTime', 'refreshRate', 'flatCurved']

class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessorFeatures
        fields = ['socket', 'series', 'generation', 'cores']

class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoardFeatures
        fields = ['socket','series','generation','fcores']

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model= RamFeatures
        fields = ['capacity','memoryType','speed']

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=PowerSupplyFeatures
        fields=['watt','rating','modular']

class GraphicsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=GraphicsCardFeatures
        fields=['chipset', 'gpuMemory']

class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoolingFeatures
        fields=['pcCooling']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CaseFeatures
        fields=['watt','caseFans', 'bundled']

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model=StorageFeatures
        fields=['capacity', 'formfactor', 'interface']

class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model= NotebookFeatures
        fields=['display', 'graphicsCard', 'ram', 'panel', 'processor', 'refreshRate', 'storage']

class ProductBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductBanner
        fields = ['id', 'image', 'product']

class ImageBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageBanner
        fields = ['id', 'image', 'name']

class AdBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdBanner
        fields = ['id', 'name', 'image', 'url']

class VideoBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoBanner
        fields = ['id', 'name', 'url']

class BrandBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandBanner
        fields = ['id', 'name', 'image', 'brand']