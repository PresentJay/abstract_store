from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("<int:item_pk>/", views.add_fav, name="add-favs"),
    path("favs/", views.SeeFavsView.as_view(), name="see-favs"),
]
