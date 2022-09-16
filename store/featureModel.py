from django.db import models
from django.core.validators import MinValueValidator
from store.models import Products

class MonitorFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='monitorFeatures', primary_key=True, db_column='id')
    featureDisplayRes = models.CharField(max_length=12, null=True, blank=True)
    featureScreenSize = models.CharField(max_length=5, null=True, blank=True)
    featurePanelType = models.CharField(max_length=5, null=True, blank=True)
    featureResponseTime = models.CharField(max_length=5, null=True, blank=True)
    featureRefreshRate = models.CharField(max_length=5, null=True, blank=True)
    featureFlatCurved = models.CharField(max_length=10, null=True, blank=True)
    
class ProcessorFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='processorFeatures', primary_key=True, db_column='id')
    featureSocket = models.CharField(max_length=20, null=True, blank=True)
    featureSeries = models.CharField(max_length=50, null=True, blank=True)
    featureGeneration = models.CharField(max_length=50, null=True, blank=True)
    featureCores = models.CharField(max_length=10, null=True, blank=True)

class MotherBoardFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='motherBoardFeatures', primary_key=True, db_column='id')
    featureSocket = models.CharField(max_length=20, null=True, blank=True)
    featureSeries = models.CharField(max_length=50, null=True, blank=True)
    featureGeneration = models.CharField(max_length=50, null=True, blank=True)
    featureCores = models.CharField(max_length=10, null=True, blank=True)

class RamFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='ramFeatures', primary_key=True, db_column='id')
    featureCapacity = models.CharField(max_length=6, null=True, blank=True)
    featureMemoryType = models.CharField(max_length=7, null=True, blank=True)
    featureSpeed = models.CharField(max_length=10, null=True, blank=True)

class PowerSupplyFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='powerSupplyFeatures', primary_key=True, db_column='id')
    featureWatt = models.CharField(max_length=10, null=True, blank=True)
    featureRating = models.CharField(max_length=10, null=True, blank=True)
    featureModular = models.CharField(max_length=10, null=True, blank=True)

class GraphicsCardFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='graphicsCardFeatures', primary_key=True, db_column='id')
    featureChipset = models.CharField(max_length=20, null=True, blank=True)
    featureGpuMemory = models.CharField(max_length=10, null=True, blank=True)

class CoolingFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='coolingFeatures', primary_key=True, db_column='id')
    featurePcCooling = models.BooleanField(default=False)

class CaseFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='caseFeatures', primary_key=True, db_column='id')
    featureWatt = models.CharField(max_length=10, null=True, blank=True)
    featureCaseFans = models.CharField(max_length=10, null=True, blank=True)
    bundled = models.BooleanField(default=False)

class StorageFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='storage', primary_key=True, db_column='id')
    featureCapacity = models.CharField(max_length=6, null=True, blank=True)
    featureFormfactor = models.CharField(max_length=10, null=True, blank=True)
    featureInterface = models.CharField(max_length=15, null=True, blank=True)
    
class NotebookFeatures(models.Model):
    product = models.OneToOneField(Products, on_delete=models.PROTECT, related_name='notebook', primary_key=True, db_column='id')
    notebookDisplay = models.CharField(max_length=20, null=True, blank=True)
    notebookGraphicsCard = models.CharField(max_length=20, null=True, blank=True)
    notebookRam = models.CharField(max_length=20, null=True, blank=True)
    notebookPanel = models.CharField(max_length=20, null=True, blank=True)
    notebookProcessor = models.CharField(max_length=20, null=True, blank=True)
    notebookRefreshRate = models.CharField(max_length=20, null=True, blank=True)
    notebookStorage = models.CharField(max_length=20, null=True, blank=True)
   