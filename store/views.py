from multiprocessing import managers
import queue
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.featureModel import *
from .models import *
from .serializers import *

@api_view(['GET'])
def category_list(request):
    queryset = Category.objects.all()
    serializer = CategorySerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def subCategory_list(request, id):
    queryset = SubCategory.objects.all().filter(category=id)
    serializer = SubCategorySerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def featured_list(request):
    queryset = FeaturedProduct.objects.all()
    serializer = FeaturedProductSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def product_banner_list(request):
    queryset = ProductBanner.objects.all()
    serializer = ProductBannerSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def image_banner_list(request):
    queryset = ImageBanner.objects.all()
    serializer = ImageBannerSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def ads_banner_list(request):
    queryset = AdBanner.objects.all()
    serializer = AdBannerSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def video_banner_list(request):
    queryset = VideoBanner.objects.all()
    serializer = VideoBannerSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def subCategory_products_list(request, id):
    queryset = Product.objects.all().filter(subCategory=id)
    serializer = SubCategorySerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def brand_list(request):
    queryset = Brand.objects.all()
    serializer = BrandSerializer(
        queryset, many=True, context={'request': request})
    print(serializer.data)
    return Response(serializer.data)

@api_view(['GET'])
def brand_products_list(request, id):
    queryset = Product.objects.all().filter(brand=id)
    serializer = SubCategorySerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def brand_banner_list(request, id):
    queryset = Product.objects.all().filter(brand=id)
    serializer = BrandBannerSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def new_products_list(request):
    queryset = Product.objects.all().filter(isNew=True)
    serializer = ProductSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def hot_products_list(request):
    queryset = Product.objects.all().filter(isDiscount=True)
    serializer = ProductSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data) 

@api_view(['GET'])
def product_details(request, id):
    product = get_object_or_404(Product, pk=id)
    serializer = ProductSerializer(product, context={'request': request})
    x = checker(serializer, id)
    images =  get_object_or_404(ProductImage, product=id)
    imageSerializer = ProductImagesSerializer(images, context={'request': request})
    y = imageSerializer.data
    z = {k: v for k, v in y.items() if v}
    x.update(z)
    return Response(x)

def checker(serializer, id):
    if serializer.data['subCategory'] == 1:
        features = get_object_or_404(MonitorFeatures, pk=id)
        data = MonitorSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 2:
        features = get_object_or_404(ProcessorFeatures, pk=id)
        data = ProcessorSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 3:
        features = get_object_or_404(MotherBoardFeatures, pk=id)
        data = MotherBoardSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 4:
        features = get_object_or_404(RamFeatures, pk=id)
        data = RamSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 5:
        features = get_object_or_404(PowerSupplyFeatures, pk=id)
        data = PowerSupplySerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 6:
        features = get_object_or_404(GraphicsCardFeatures, pk=id)
        data = GraphicsCardSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 7:
        features = get_object_or_404(CoolingFeatures, pk=id)
        data = CoolingSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 8:
        features = get_object_or_404(CaseFeatures, pk=id)
        data = CaseSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 9:
        # This is for M.2 Only
        features = get_object_or_404(StorageFeatures, pk=id)
        data = StorageSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['subCategory'] == 10:
        features = get_object_or_404(NotebookFeatures, pk=id)
        data = NoteBookSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    else:
        return serializer.data
