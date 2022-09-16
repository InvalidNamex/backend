from django.db import models
from django.contrib.auth.models import AbstractUser
from smart_selects.db_fields import ChainedForeignKey

class Collections(models.Model):
    collectionName = models.CharField(max_length=255)
    collectionImage = models.ImageField(upload_to='collections', blank=True)
    def __str__(self) -> str:
        return self.collectionName
    class Meta:
        ordering = ['collectionName']

class SubCollections(models.Model):
    subCollectionName = models.CharField(max_length=255)
    subCollectionMainCollection = models.ForeignKey(Collections, on_delete=models.PROTECT)
    subcollectionImage = models.ImageField(upload_to='subCollections', blank=True)
    def __str__(self) -> str:
        return self.subCollectionName
    class Meta:
        ordering = ['subCollectionName']

class Products(models.Model):
    productName = models.CharField(max_length=255)
    productPrice = models.DecimalField(max_digits=8, decimal_places=2)
    productSlug = models.SlugField()
    productAvailability = models.BooleanField(default=False)
    productDescription = models.TextField(null=True, blank=True)
    productSKU = models.CharField(max_length=255, null=True, blank=True)
    productCollection = models.ForeignKey(Collections, on_delete=models.PROTECT, related_name='products')
    productSubCollection = ChainedForeignKey(SubCollections, chained_field='productCollection', chained_model_field='subCollectionMainCollection')
    productBrand = models.ForeignKey("Brands", on_delete=models.PROTECT, related_name='products', null=True, blank=True)
    productModel = models.CharField(max_length=255, null=True, blank=True)
    productLastUpdate = models.DateTimeField(auto_now=True)
    productRating = models.SmallIntegerField()
    def __str__(self) -> str:
        return self.productName
    
    class Meta():
        ordering = ['productName']

class Brands(models.Model):
    brandName = models.CharField(max_length=255)
    brandImage = models.ImageField(upload_to='brands', blank=True)
    def __str__(self) -> str:
        return self.brandName
    class Meta:
        ordering = ['brandName']

class Banners(models.Model):
    bannerImage = models.ImageField(upload_to='banners', blank=True)
    bannerProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    
    class Meta():
        ordering = ['bannerProduct']

class Promotions(models.Model):
    promotionName = models.CharField(max_length=255)
    promotionDescription = models.TextField(blank=True)
    promotionDiscount = models.PositiveSmallIntegerField()
    promotionIsPercentage = models.BooleanField(default=False)
    promotionIsActive = models.BooleanField(default=True)

class ProductImages(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    imageOne = models.ImageField(upload_to='products', blank=True)
    imageTwo = models.ImageField(upload_to='products', blank=True)
    imageThree = models.ImageField(upload_to='products', blank=True)
    imageFour = models.ImageField(upload_to='products', blank=True)
    imageFive = models.ImageField(upload_to='products', blank=True)
    imageSix = models.ImageField(upload_to='products', blank=True)
    imageSeven = models.ImageField(upload_to='products', blank=True)
    imageEight = models.ImageField(upload_to='products', blank=True)
    imageNine = models.ImageField(upload_to='products', blank=True)
    imageTen = models.ImageField(upload_to='products', blank=True)

    def __str__(self) -> str:
        return self.product.productName
    
    class Meta():
        ordering = ['product']

class FeaturedProducts(models.Model):
    featuredProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    featuredProductCreatedAt = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.featuredProduct.productName

class Customers(AbstractUser):
    # customerFirstName = models.CharField(max_length=255)
    # customerLastName = models.CharField(max_length=255)
    customerEmail = models.EmailField(unique=True)
    # customerPhone = models.CharField(max_length=255)
    # customerCreationDate = models.DateTimeField(auto_now_add=True)
    # customerIsVerified = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.customerFirstName} {self.customerLastName}'

class Cart(models.Model):
    cartCreatedAt = models.DateTimeField(auto_now_add=True)
    cartCustomer = models.ForeignKey(Customers, on_delete=models.CASCADE)

class Addresses(models.Model):
    addressCustomer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    addressTitle = models.CharField(max_length=255)
    addressLineOne = models.CharField(max_length=255)
    addressLineTwo = models.CharField(max_length=255, blank=True)
    addressDescription =  models.CharField(max_length=255, blank=True)

class WishList(models.Model):
    wishListCustomer = models.ForeignKey(Customers, on_delete=models.PROTECT)
    wishListProducts = models.ForeignKey(Products, on_delete=models.PROTECT)
    wishListLikedDate = models.DateTimeField(auto_now=True)
    
    class Meta():
        ordering = ['wishListProducts']

class PurchaseItem(models.Model):
    purchaseItemCart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    purchaseItemProduct = models.ForeignKey(Products, on_delete=models.CASCADE)
    purchaseItemQuantity = models.PositiveSmallIntegerField()
    purchaseItemUnitPrice = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta():
        ordering = ['purchaseItemCart']
