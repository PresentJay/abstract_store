from django.db import models
from core import models as core_models

# Create your models here.
class BoardBaseModel(core_models.TimeStampedModel):
    title = models.CharField(max_length=80)
    description = models.TextField()
    
    class Meta:
        abstract = True

class Review(BoardBaseModel):
    user = models.ForeignKey("users.User", related_name="reviews", on_delete=models.CASCADE)
    grade = models.DecimalField(max_digits=5, decimal_places=0, null=True)
    
    def __str__(self):
        return self.title

class Question(BoardBaseModel):
    user = models.ForeignKey("users.User", related_name="questions", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Notice(BoardBaseModel):
    user = models.ForeignKey("users.User", related_name="notices", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
class Answer(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField()
    review = models.ForeignKey("Review",related_name="answers" , on_delete=models.CASCADE, null = True, blank=True)
    question = models.ForeignKey("Question",related_name="answers" , on_delete=models.CASCADE, null = True, blank=True)
    notice = models.ForeignKey("Notice",related_name="answers" , on_delete=models.CASCADE, null = True, blank=True)
    
    def __str__(self):
        return self.title