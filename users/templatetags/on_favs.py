from django import template
from users import models as user_models

register = template.Library()

@register.simple_tag(takes_context=True)
def on_favs(context, item):
    user = context.request.user
    the_list = user_models.FavList.objects.get_or_none(user=user)
    if the_list is not None:
        return item in the_list.items.all()
    return False