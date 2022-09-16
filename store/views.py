from email.mime import image
from django.db.models.aggregates import Count
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from store.featureModel import *
from .models import *
from .serializers import *

@api_view(['GET'])
def collection_list(request):
    queryset = Collections.objects.all()
    serializer = CollectionSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def subCollection_list(request, id):
    queryset = SubCollections.objects.all().filter(subCollectionMainCollection=id)
    serializer = SubCollectionSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def featured_list(request):
    queryset = FeaturedProducts.objects.all()
    serializer = FeaturedProductsSerializer(
        queryset, many=True, context={'request': request})
    return Response(serializer.data)

@api_view(['GET'])
def product_details(request, id):
    product = get_object_or_404(Products, pk=id)
    serializer = ProductSerializer(product, context={'request': request})
    x = checker(serializer, id)
    images =  get_object_or_404(ProductImages, product=id)
    imageSerializer = ProductImagesSerializer(images, context={'request': request})
    y = imageSerializer.data
    z = {k: v for k, v in y.items() if v}
    x.update(z)
    return Response(x)



def checker(serializer, id):
    if serializer.data['productSubCollection'] == 1:
        features = get_object_or_404(MonitorFeatures, pk=id)
        data = MonitorSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 2:
        features = get_object_or_404(ProcessorFeatures, pk=id)
        data = ProcessorSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 3:
        features = get_object_or_404(MotherBoardFeatures, pk=id)
        data = MotherBoardSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 4:
        features = get_object_or_404(RamFeatures, pk=id)
        data = RamSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 5:
        features = get_object_or_404(PowerSupplyFeatures, pk=id)
        data = PowerSupplySerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 6:
        features = get_object_or_404(GraphicsCardFeatures, pk=id)
        data = GraphicsCardSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 7:
        features = get_object_or_404(CoolingFeatures, pk=id)
        data = CoolingSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 8:
        features = get_object_or_404(CaseFeatures, pk=id)
        data = CaseSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 9:
        # This is for M.2 Only
        features = get_object_or_404(StorageFeatures, pk=id)
        data = StorageSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    elif serializer.data['productSubCollection'] == 10:
        features = get_object_or_404(NoteBookSerializer, pk=id)
        data = NoteBookSerializer(features)
        x = serializer.data
        y = data.data
        x.update(y)
        return x
    else:
        return serializer.data
