from django.db import models
from core import models as core_models

# Create your models here.
class ListBaseModel(core_models.TimeStampedModel):
    
    """ List Base Model """
    
    count = models.IntegerField(default=1)
    price = models.IntegerField()
    
    class Meta:
        abstract = True

class OrderList(ListBaseModel):
    STATUS_RECEIVING = "주문 접수"
    STATUS_PROCESSING = "처리 중"
    STATUS_DLIVERY_PREPARING = "배송 준비중"
    STATUS_DLIVERY = "배송중"
    STATUS_DLIVERY_COMPLETED = "배송 완료"
    STATUS_CANCELED = "취소"
    
    STATUS_CHOICES = (
        (STATUS_RECEIVING, "주문 접수"),
        (STATUS_PROCESSING, "처리 중"),
        (STATUS_DLIVERY_PREPARING, "배송 준비중"),
        (STATUS_DLIVERY, "배송중"),
        (STATUS_DLIVERY_COMPLETED, "배송 완료"),
        (STATUS_CANCELED, "취소"),
    )
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_RECEIVING)
    item = models.ForeignKey("items.Item", related_name="orderlists", on_delete=models.CASCADE)
    option = models.ForeignKey("items.Option", related_name="orderlists", on_delete=models.CASCADE, blank=True)
    user = models.ForeignKey("users.User", related_name="orderlists", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name
