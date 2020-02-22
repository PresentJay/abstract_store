from django.db import models
from core import models as core_models

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.tag_name
    
class Option(models.Model):
    option_name = models.CharField(max_length=1024)
    extra_money = models.IntegerField()
    
    def __str__(self):
        return self.option_name
    
class Item(core_models.TimeStampedModel):
    name = models.CharField(max_length=1024)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    product = models.TextField()
    status = models.BooleanField(default=True)
    tag = models.ManyToManyField("Tag", related_name="items", blank=True)
    option = models.ManyToManyField("Option", related_name="items", blank=True )
    
    status.boolean = True
    
    def __str__(self):
        return self.name