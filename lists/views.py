from django.shortcuts import redirect, reverse
from django.views.generic import TemplateView
from items import models as item_models
from users import models as user_models
from . import models

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
    
def add_fav(request, item_pk):
    item = item_models.Item.objects.get_or_none(pk=item_pk)
    if item is not None:
        the_list, _ = models.FavList.objects.get_or_create(user=request.user)
        the_list.items.add(item)
    return redirect(reverse("items:detail", kwargs={"pk":item_pk}))

class SeeFavsView(TemplateView):
    
    template_name = "lists/list_detail.html"