from django.db import models
from core import models as core_models

# Create your models here.
class Review(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    item = models.ForeignKey("items.Item", related_name="reviews", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    def get_photo(self):
        try:
            photo, = self.photos.all()[:1]
            return photo.file.url
        except ValueError:
            return None
        
class Photo(models.Model):
    file = models.ImageField(upload_to="review_photos")
    review = models.ForeignKey("Review",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    
class Recomment(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.TextField()
    user = models.ForeignKey("users.User", related_name="recomments", on_delete=models.CASCADE)
    review = models.ForeignKey("Review", related_name="recomments", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
