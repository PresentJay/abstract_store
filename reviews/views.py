from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from items import models as item_models
from . import forms, models

# Create your views here.
def create_review(request, item_pk):
    title = request.POST['title']
    content = request.POST['content']
    if title != "" and content != "":
        item = item_models.Item.objects.get(pk=item_pk)
        user = request.user
        
        review = models.Review.objects.create(
            item = item,
            user = user,
            title = title,
            content = content,
        )
        review.save()
        return redirect(reverse("items:detail", kwargs={"pk":item.pk}))
    else:
        return redirect(reverse("core:home"))
    
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