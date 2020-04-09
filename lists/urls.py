from django.urls import path
from . import views

app_name = "lists"

urlpatterns = [
    path("<int:item_pk>/order/", views.create_order, name="order"),
]