from django.db import models
from core import models as core_models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.tag_name
    
class Category(models.Model):
    category_name = models.CharField(max_length=1024)
    
    def __str__(self):
        return self.category_name
    
class Option(models.Model):
    option_name = models.CharField(max_length=1024)
    extra_money = models.IntegerField()
    
    def __str__(self):
        return self.option_name
    
class Item(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    shorten_description = models.TextField(blank=True)
    tag = models.ManyToManyField("Tag", related_name="items", blank=True)
    category = models.ManyToManyField("Category", related_name="items", blank=True)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    description = RichTextUploadingField(null=True, blank=True)
    option = models.ManyToManyField("Option", related_name="items", blank=True)
    count = models.IntegerField()
    owner = models.ForeignKey("users.User", related_name="items", on_delete=models.CASCADE)
    
    status.boolean = True
    
    def __str__(self):
        return self.name
    
class Thumbnail(models.Model):
    file = models.ImageField(upload_to="item_thumbnails")
    item = models.ForeignKey("items.Item",related_name="item_thumbnails" , on_delete=models.CASCADE, null = True, blank=True)
    
class Photo(models.Model):
    file = models.ImageField(upload_to="item_photos")
    item = models.ForeignKey("Item",related_name="item_photos" , on_delete=models.CASCADE, null = True, blank=True)