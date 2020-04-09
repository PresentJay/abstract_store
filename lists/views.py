from django.shortcuts import render, redirect, reverse
from . import models
from items import models as item_models
from users import models as user_models

# Create your views here.
def create_order(request, item_pk):
    user = request.user
    option_pk = request.POST['option']
      
    try:
        item = item_models.Item.objects.get(pk=item_pk)
        option = item_models.Option.objects.get(pk=option_pk)
        price = (item.price + option.extra_money)
        order = models.OrderList.objects.create(
            item=item,
            option=option,
            user=user,
            price=price,
        )
        order.save()
        return redirect(reverse("core:home"))
    except models.OrderList.DoesNotExist:
        return redirect(reverse("core:home"))