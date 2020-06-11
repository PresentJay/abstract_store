from django.shortcuts import redirect,reverse
from django.views.generic import TemplateView
from items import models as item_models
from . import models

# Create your views here.
def create_order(request, item_pk):
    user = request.user
    option_pk = request.POST['option']
      
    try:
        item = item_models.Item.objects.get(pk=item_pk)
        option = item_models.Option.objects.get(pk=option_pk)
        items = models.OrderingItem.objects.create(item = item)
        items.option.add(option)
        order = models.Order.objects.create(
            user=user,
            address = user.address1,
            postal_code = user.postal_code,
        )
        order.items.add(items)
        order.save()
        return redirect(reverse("orders:detail"))
    except models.Order.DoesNotExist:
        return redirect(reverse("core:home"))
  
class OrderList(TemplateView):
    
    template_name = "orders/order_detail.html"