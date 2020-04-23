from django import template
from lists import models as list_models

register = template.Library()

@register.simple_tag(takes_context=True)
def on_favs(context, item):
    user = context.request.user
    the_list = list_models.FavList.objects.get_or_none(user=user)
    if the_list is not None:
        return item in the_list.items.all()
    return False