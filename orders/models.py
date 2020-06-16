from django.db import models
from core import models as core_models

class Order(core_models.TimeStampedModel):
    ORDER_CREATED = "order_created"
    WAIT_CONFIRM = "wait_confirm"
    PAY_CONFIRMED = "pay_confirmed"
    PAY_CANCELED = "pay_canceled"
    STARTED_SHIPPING = "started_shipping"
    ENDED_SHIPPING = "ended_shipping"
    
    STATE_CHOICES = (
        (ORDER_CREATED, "order_created"),
        (WAIT_CONFIRM, "wait_confirm"),
        (PAY_CONFIRMED, "pay_confirmed"),
        (PAY_CANCELED, "pay_canceled"),
        (STARTED_SHIPPING, "started_shipping"),
        (ENDED_SHIPPING, "ended_shipping"),
    )
    
    user = models.ForeignKey("users.User", related_name="orders", on_delete=models.CASCADE)
    items = models.ManyToManyField("orders.OrderingItem", related_name="orders", blank=True)
    state = models.CharField(max_length=50, choices=STATE_CHOICES, default=ORDER_CREATED)
    receipt_id = models.CharField(max_length=24, blank=True)
    address = models.CharField(max_length=128, blank=True, null=True)
    postal_code = models.CharField(max_length=7, blank=True, null=True)
    confirmed_date = models.DateTimeField(blank=True, null=True)
    shipping_started_date = models.DateTimeField(blank=True, null=True)
    completed_date = models.DateTimeField(blank=True, null=True)
    
    def __str__(self):
        try:
            item_list = self.items.all()
            title = item_list[0].item.name
            if item_list.count() > 0:
                title += " 외 " + str(item_list.count()) + "개" 
            return title
        except:
            return "Error"
    
    def thumnail(self):
        item = self.items.all()[0]
        photo = item.item.photos.all()[0]
        return photo.file.url
    
class OrderingItem(models.Model):
    item = models.ForeignKey("items.Item", related_name="orderingitems", on_delete=models.CASCADE)
    option = models.ManyToManyField("items.Option",related_name="orderingitems", blank=True)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.item.name