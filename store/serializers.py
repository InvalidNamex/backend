from dataclasses import field
from rest_framework import serializers
from store.featureModel import *
from store.models import Addresses, Brands, Cart, Customers, FeaturedProducts, Banners, Products, Collections, PurchaseItem, SubCollections, ProductImages, Promotions, WishList

class CollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collections
        fields = ['id', 'collectionName', 'collectionImage']

class SubCollectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCollections
        fields = ['id', 'subCollectionName', 'subCollectionMainCollection', 'subcollectionImage']

class BrandsSerializer(serializers.Serializer):
    model = Brands
    fields = ['id', 'brandName', 'brandImage']

class PromotionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Promotions
        fields = ['id', 'promotionName', 'promotionDescription', 'promotionDiscount', 'promotionIsPercentage', 'promotionIsActive' ]

class FeaturedProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeaturedProducts
        fields = ['id', 'featuredProduct' , 'featuredProductCreatedAt']

class BannersSerializer(serializers.Serializer):
    class Meta:
        model = Banners
        fields = ['id', 'bannerImage', 'bannerProduct']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ['id', 'productName', 'productPrice', 'productSlug', 'productAvailability', 'productDescription', 'productSKU', 'productCollection', 'productSubCollection', 'productBrand', 'productModel', 'productLastUpdate']

class ProductImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = ['id', 'product', 'imageOne', 'imageTwo', 'imageThree', 'imageFour', 'imageFive', 'imageSix', 'imageSeven', 'imageEight', 'imageNine', 'imageTen']

class CustomersSerializer(serializers.ModelSerializer):
    model = Customers
    fields = ['id', 'customerFirstName', 'customerLastName', 'customerEmail', 'customerPhone', 'customerCreationDate', 'customerIsVerified']

class AddressesSerializer(serializers.ModelSerializer):
    model = Addresses
    fields = ['id', 'addressCustomer','addressTitle', 'addressLineOne','addressLineTwo', 'addressDescription']

class WishListSerializer(serializers.ModelSerializer):
    model = WishList
    fields = ['id', 'wishListCustomer', 'wishListProducts', 'wishListLikedDate']

class CartSerializer(serializers.ModelSerializer):
    model = Cart
    fields = ['id', 'CreatedAt', 'cartCustomer']

class PurchaseItemSerializer(serializers.ModelSerializer):
    model = PurchaseItem
    fields = ['id', 'purchaseItemCart', 'purchaseItemProduct', 'purchaseItemQuantity', 'purchaseItemUnitPrice']

class ProductsFeatures(serializers.ModelField):
    id = serializers.IntegerField()
    productPrice = serializers.DecimalField(max_digits=8, decimal_places=2)
    price_with_tax = serializers.SerializerMethodField(method_name='calc_tax')
    def calc_tax(self, product:Products):
        return product.unit_price * 1.1

class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = MonitorFeatures
        fields = ['product', 'featureDisplayRes', 'featureScreenSize', 'featurePanelType', 'featureResponseTime', 'featureRefreshRate', 'featureFlatCurved']

class ProcessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessorFeatures
        fields = ['product', 'featureSocket', 'featureSeries', 'featureGeneration', 'featureCores']

class MotherBoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotherBoardFeatures
        fields = ['product','featureSocket','featureSeries','featureGeneration','featureCores']

class RamSerializer(serializers.ModelSerializer):
    class Meta:
        model= RamFeatures
        fields = ['product','featureCapacity','featureMemoryType','featureSpeed']

class PowerSupplySerializer(serializers.ModelSerializer):
    class Meta:
        model=PowerSupplyFeatures
        fields=['product','featureWatt','featureRating','featureModular']

class GraphicsCardSerializer(serializers.ModelSerializer):
    class Meta:
        model=GraphicsCardFeatures
        fields=['product', 'featureChipset', 'featureGpuMemory']

class CoolingSerializer(serializers.ModelSerializer):
    class Meta:
        model=CoolingFeatures
        fields=['product', 'featurePcCooling']

class CaseSerializer(serializers.ModelSerializer):
    class Meta:
        model=CaseFeatures
        fields=['product','featureWatt','featureCaseFans', 'bundled']

class StorageSerializer(serializers.ModelSerializer):
    class Meta:
        model=StorageFeatures
        fields=['product', 'featureCapacity', 'featureFormfactor', 'featureInterface']

class NoteBookSerializer(serializers.ModelSerializer):
    class Meta:
        model=NotebookFeatures
        fields=['product', 'notebookDisplay', 'notebookGraphicsCard', 'notebookRam', 'notebookPanel', 'notebookProcessor', 'notebookRefreshRate', 'notebookStorage']

