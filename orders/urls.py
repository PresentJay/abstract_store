from django.urls import path
from . import views

app_name = "orders"

urlpatterns = [
    path("<int:item_pk>/addorder/", views.create_order, name="add-order"),
    path("order/", views.OrderList.as_view(), name="detail"),
]