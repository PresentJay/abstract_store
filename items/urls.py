from django.urls import path
from . import views

app_name = "items"

urlpatterns = [
    path("<int:pk>/", views.ItemDetail.as_view(), name="detail"),
]