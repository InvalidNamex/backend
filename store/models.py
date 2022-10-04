from django.db import models
from django.contrib.auth.models import AbstractUser
from smart_selects.db_fields import ChainedForeignKey
from autoslug import AutoSlugField

class Category(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='collections', blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='sub-collections', blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    afterPrice = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    isDiscount = models.BooleanField(default=False)
    isNew = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from='name')
    availability = models.BooleanField(default=False)
    description = models.TextField(null=True, blank=True)
    sku = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='product')
    subCategory = ChainedForeignKey(SubCategory, chained_field='category', chained_model_field='category')
    brand = models.ForeignKey("Brand", on_delete=models.PROTECT, related_name='product', null=True, blank=True)
    model = models.CharField(max_length=255, null=True, blank=True)
    lastUpdate = models.DateTimeField(auto_now=True)
    rating = models.SmallIntegerField()
    def __str__(self) -> str:
        return self.name
    
    class Meta():
        ordering = ['name']

class Brand(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='brands', blank=True)
    def __str__(self) -> str:
        return self.name
    class Meta:
        ordering = ['name']

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    discount = models.PositiveSmallIntegerField()
    isPercentage = models.BooleanField(default=False)
    isActive = models.BooleanField(default=True)

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
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
        return self.product.name
    
    class Meta():
        ordering = ['product']

class FeaturedProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.product.name

class Customer(AbstractUser):
    # customerFirstName = models.CharField(max_length=255)
    # customerLastName = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    # customerPhone = models.CharField(max_length=255)
    # customerCreationDate = models.DateTimeField(auto_now_add=True)
    # customerIsVerified = models.BooleanField(default=False)
    # def __str__(self):
    #     return f'{self.customerFirstName} {self.customerLastName}'

class Cart(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    title = models.CharField(max_length=255)
    lineOne = models.CharField(max_length=255)
    lineTwo = models.CharField(max_length=255, blank=True)
    description =  models.CharField(max_length=255, blank=True)

class WishList(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    products = models.ForeignKey(Product, on_delete=models.PROTECT)
    likedDate = models.DateTimeField(auto_now=True)
    
    class Meta():
        ordering = ['products']

class PurchaseItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
    unitPrice = models.DecimalField(max_digits=8, decimal_places=2)
    
    class Meta():
        ordering = ['cart']

class BrandBanner(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    image = models.ImageField(upload_to='brand-banners')
    name = models.CharField(max_length=255, blank=True)
    def __str__(self) -> str:
        return self.name

class VideoBanner(models.Model):
    url = models.CharField(max_length=255)
    name = models.CharField(max_length=255, blank=True)
    def __str__(self) -> str:
        return self.name


class AdBanner(models.Model):
    url = models.URLField(max_length=300)
    image =  models.ImageField(upload_to='ads-banners')
    name = models.CharField(max_length=255, blank=True)
    def __str__(self) -> str:
        return self.name


class ImageBanner(models.Model):
    image = models.ImageField(upload_to='image-banner', blank=True)
    name = models.CharField(max_length=255, blank=True)
    def __str__(self) -> str:
        return self.name

    
class ProductBanner(models.Model):
    image = models.ImageField(upload_to='product-banner', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return self.product.name