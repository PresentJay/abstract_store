from django.db import models
from boards import models as boards_model
from items import models as items_model

# Create your models here.
class Photo(models.Model):
    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="photos")
    
    review = models.ForeignKey("boards.Review",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    question = models.ForeignKey("boards.Question",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    notice = models.ForeignKey("boards.Notice",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    answer = models.ForeignKey("boards.Answer",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    item = models.ForeignKey("items.Item",related_name="photos" , on_delete=models.CASCADE, null = True, blank=True)
    
    def __str__(self):
        return self.caption