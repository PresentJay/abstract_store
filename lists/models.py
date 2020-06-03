from django.db import models
from core import models as core_models

<<<<<<< HEAD
class OrderList(core_models.TimeStampedModel):
    STATUS_RECEIVING = "주문 접수"
    STATUS_PROCESSING = "처리 중"
    STATUS_DLIVERY_PREPARING = "배송 준비중"
    STATUS_DLIVERY = "배송중"
    STATUS_DLIVERY_COMPLETED = "배송 완료"
    STATUS_CANCELED = "취소"
    
=======
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

>>>>>>> adjusting branches
    STATUS_CHOICES = (
        (STATUS_RECEIVING, "주문 접수"),
        (STATUS_PROCESSING, "처리 중"),
        (STATUS_DLIVERY_PREPARING, "배송 준비중"),
        (STATUS_DLIVERY, "배송중"),
        (STATUS_DLIVERY_COMPLETED, "배송 완료"),
        (STATUS_CANCELED, "취소"),
    )
<<<<<<< HEAD
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default=STATUS_RECEIVING)
    item = models.ForeignKey("items.Item", related_name="orderlists", on_delete=models.CASCADE)
    option = models.ForeignKey("items.Option", related_name="orderlists", on_delete=models.CASCADE, blank=True)
    count = models.IntegerField(default=1)
    price = models.IntegerField()
    user = models.ForeignKey("users.User", related_name="orderlists", on_delete=models.CASCADE)
    
    def __str__(self):
        return self.user.name
    
class FavList(core_models.TimeStampedModel):
    
    user = models.OneToOneField("users.User",related_name="list" , on_delete=models.CASCADE)
    items = models.ManyToManyField("items.Item",related_name="lists" , blank=True)
    
    def __str__(self):
        return self.user.name
=======
    delivery_status = models.CharField(
        max_length=50, choices=STATUS_CHOICES, default=STATUS_PREPARING)
    user = models.ForeignKey(
        "users.User", related_name="orderlists0", on_delete=models.CASCADE)
    option = models.ManyToManyField(
        "items.Option", related_name="orderlists", blank=True)

    def __str__(self):
        return self.name


class WishList(ListBaseModel):
    user = models.ForeignKey(
        "users.User", related_name="wishlists", on_delete=models.CASCADE)
    option = models.ManyToManyField(
        "items.Option", related_name="wishlists", blank=True)

    def __str__(self):
        return self.name


class ShoppingList(ListBaseModel):
    user = models.ForeignKey(
        "users.User", related_name="shoppinglists", on_delete=models.CASCADE)
    option = models.ManyToManyField(
        "items.Option", related_name="shoppinglists", blank=True)

    def __str__(self):
        return self.name
>>>>>>> adjusting branches
