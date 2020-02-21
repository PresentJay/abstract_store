from django.db import models
from core import models as core_models

# Create your models here.
class ListBaseModel(core_models.TimeStampedModel):
    
    """ List Base Model """
    
    image = models.ImageField()
    name = models.CharField(max_length=1024)
    count = models.IntegerField()
    price = models.IntegerField()
    
    class Meta:
        abstract = True

class OrderList(ListBaseModel):
    STATUS_PREPARING = "Preparing for delivery"
    STATUS_SHIPPING = "Shipping"
    STATUS_COMPLETED = "Delivery completed"
    STATUS_CANCELED = "Canceled"
    
    STATUS_CHOICES = (
        (STATUS_PREPARING, "Preparing for delivery"),
        (STATUS_SHIPPING, "Shipping"),
        (STATUS_COMPLETED, "Delivery completed"),
        (STATUS_CANCELED, "Canceled"),
    )
    delivery_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_PREPARING)
    user = models.ForeignKey("users.User", related_name="orderlists", on_delete=models.CASCADE)
    option = models.ManyToManyField("items.Option", related_name="orderlists", blank=True)
    
    def __str__(self):
        return self.name

class WishList(ListBaseModel):
    user = models.ForeignKey("users.User", related_name="wishlists", on_delete=models.CASCADE)
    option = models.ManyToManyField("items.Option", related_name="wishlists", blank=True)
    
    def __str__(self):
        return self.name

class ShoppingList(ListBaseModel):
    user = models.ForeignKey("users.User", related_name="shoppinglists", on_delete=models.CASCADE)
    option = models.ManyToManyField("items.Option", related_name="shoppinglists", blank=True)

    def __str__(self):
        return self.name
