from django.db import models
from store.models import Product

class MonitorFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='monitorFeatures', primary_key=True, db_column='id')
    displayRes = models.CharField(max_length=12, null=True, blank=True)
    screenSize = models.CharField(max_length=5, null=True, blank=True)
    panelType = models.CharField(max_length=5, null=True, blank=True)
    responseTime = models.CharField(max_length=5, null=True, blank=True)
    refreshRate = models.CharField(max_length=5, null=True, blank=True)
    flatCurved = models.CharField(max_length=10, null=True, blank=True)
    
class ProcessorFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='processorFeatures', primary_key=True, db_column='id')
    socket = models.CharField(max_length=20, null=True, blank=True)
    series = models.CharField(max_length=50, null=True, blank=True)
    generation = models.CharField(max_length=50, null=True, blank=True)
    cores = models.CharField(max_length=10, null=True, blank=True)

class MotherBoardFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='motherBoardFeatures', primary_key=True, db_column='id')
    socket = models.CharField(max_length=20, null=True, blank=True)
    series = models.CharField(max_length=50, null=True, blank=True)
    generation = models.CharField(max_length=50, null=True, blank=True)
    cores = models.CharField(max_length=10, null=True, blank=True)

class RamFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='ramFeatures', primary_key=True, db_column='id')
    capacity = models.CharField(max_length=6, null=True, blank=True)
    memoryType = models.CharField(max_length=7, null=True, blank=True)
    speed = models.CharField(max_length=10, null=True, blank=True)

class PowerSupplyFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='powerSupplyFeatures', primary_key=True, db_column='id')
    watt = models.CharField(max_length=10, null=True, blank=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    fmodular = models.CharField(max_length=10, null=True, blank=True)

class GraphicsCardFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='graphicsCardFeatures', primary_key=True, db_column='id')
    chipset = models.CharField(max_length=20, null=True, blank=True)
    gpuMemory = models.CharField(max_length=10, null=True, blank=True)

class CoolingFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='coolingFeatures', primary_key=True, db_column='id')
    pcCooling = models.BooleanField(default=False)

class CaseFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='caseFeatures', primary_key=True, db_column='id')
    watt = models.CharField(max_length=10, null=True, blank=True)
    caseFans = models.CharField(max_length=10, null=True, blank=True)
    bundled = models.BooleanField(default=False)

class StorageFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='storage', primary_key=True, db_column='id')
    capacity = models.CharField(max_length=6, null=True, blank=True)
    formfactor = models.CharField(max_length=10, null=True, blank=True)
    interface = models.CharField(max_length=15, null=True, blank=True)
    
class NotebookFeatures(models.Model):
    product = models.OneToOneField(Product, on_delete=models.PROTECT, related_name='notebook', primary_key=True, db_column='id')
    display = models.CharField(max_length=100, null=True, blank=True)
    graphicsCard = models.CharField(max_length=100, null=True, blank=True)
    ram = models.CharField(max_length=100, null=True, blank=True)
    panel = models.CharField(max_length=100, null=True, blank=True)
    processor = models.CharField(max_length=100, null=True, blank=True)
    refreshRate = models.CharField(max_length=100, null=True, blank=True)
    storage = models.CharField(max_length=100, null=True, blank=True)
   