from django.urls import path
from items import views as item_views

app_name = "core"

urlpatterns = [
    path("", item_views.HomeView.as_view(), name="home"),
]
