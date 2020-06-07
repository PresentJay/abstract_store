from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("<int:item_pk>/", views.add_fav, name="add-favs"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
    path("<int:item_pk>/order/", views.create_order, name="order"),
    path("orderlists/", views.OrderList.as_view(), name="orderlists"),
]