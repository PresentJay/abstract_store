from django.db import models
from core import models as core_models

# Create your models here.
class Question(core_models.TimeStampedModel):
    STATUS_UNANSWERED = "미답변"
    STATUS_ANSWERED = "답변완료"
    
    STATUS_CHOICES = (
        (STATUS_UNANSWERED, "미답변"),
        (STATUS_ANSWERED, "답변완료"),
    )
    
    answer_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_UNANSWERED)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    user = models.ForeignKey("users.User", related_name="questions", on_delete=models.CASCADE)
    item = models.ForeignKey("items.Item", related_name="questions", on_delete=models.CASCADE, blank=True)
    
    def __str__(self):
        return self.title
    
class Photo(models.Model):
    file = models.ImageField(upload_to="question_photos")
    question = models.ForeignKey("Question",related_name="questions" , on_delete=models.CASCADE, null = True, blank=True)
    
class Answer(core_models.TimeStampedModel):
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=50)
    user = models.ForeignKey("users.User", related_name="answers", on_delete=models.CASCADE)
    question = models.ForeignKey("Question", related_name="answers", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title