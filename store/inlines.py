from . import featureModel
from django.contrib import admin
from . import models

class MonitorInline(admin.StackedInline):
    model = featureModel.MonitorFeatures
    extra = 0
    max_num = 1

class ProcessorsInline(admin.StackedInline):
    model = featureModel.ProcessorFeatures
    extra = 0
    max_num = 1

class MotherBoardInline(admin.StackedInline):
    model = featureModel.MotherBoardFeatures
    extra = 0
    max_num = 1

class RamInline(admin.StackedInline):
    model = featureModel.RamFeatures
    extra = 0
    max_num = 1

class PowerSupplyInline(admin.StackedInline):
    model = featureModel.PowerSupplyFeatures
    extra = 0
    max_num = 1

class GraphicsCardInline(admin.StackedInline):
    model = featureModel.GraphicsCardFeatures
    extra = 0
    max_num = 1

class CoolingInline(admin.StackedInline):
    model = featureModel.CoolingFeatures
    extra = 0
    max_num = 1

class CaseInline(admin.StackedInline):
    model = featureModel.CaseFeatures
    extra = 0
    max_num = 1

class StorageInline(admin.StackedInline):
    model = featureModel.StorageFeatures
    extra = 0
    max_num = 1

class NotebookInline(admin.StackedInline):
    model = featureModel.NotebookFeatures
    extra = 0
    max_num = 1
    

class AddressesInline(admin.StackedInline):
    model = models.Address
    extra = 0
    max_num: 1

class WishListInline(admin.StackedInline):
    model = models.WishList
    extra = 0
    max_num = 1

class CartInline(admin.StackedInline):
    model = models.Cart
    extra = 0
    max_num = 1
