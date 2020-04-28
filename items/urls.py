from django.urls import path
from . import views

app_name = "items"

urlpatterns = [
    path("<int:pk>/", views.ItemDetail.as_view(), name="detail"),
    path("create/", views.CreateItemView.as_view(), name="create"),
]