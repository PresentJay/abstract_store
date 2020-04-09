from django.db import models
from core import models as core_models
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
    name = models.CharField(max_length=1024)
    extra_money = models.IntegerField()
    item = models.ForeignKey("Item", related_name="options", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Item(core_models.TimeStampedModel):
    name = models.CharField(max_length=80)
    shorten_description = models.TextField(blank=True)
    tag = models.ManyToManyField("Tag", related_name="items", blank=True)
    category = models.ManyToManyField("Category", related_name="items", blank=True)
    status = models.BooleanField(default=True)
    price = models.IntegerField()
    description = RichTextUploadingField(null=True, blank=True)
    count = models.IntegerField()
    owner = models.ForeignKey("users.User", related_name="items", on_delete=models.CASCADE)
    
    status.boolean = True
    
    def __str__(self):
        return self.name
    
    def thumbnail(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None
        
    def get_option(self):
        try:
            option, = self.options.all()
            return option
        except ValueError:
            return None
    
class Photo(models.Model):
    file = models.ImageField(upload_to="item_photos")
    item = models.ForeignKey("Item",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)