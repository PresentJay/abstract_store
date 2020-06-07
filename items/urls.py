from django.urls import path
from . import views

app_name = "items"

urlpatterns = [
    path("<int:pk>/", views.ItemDetail.as_view(), name="detail"),
    path("create/", views.CreateItemView.as_view(), name="create"),
    path("<int:pk>/edit/", views.EditItemView.as_view(), name="edit"),
    path("<int:pk>/photos/", views.ItemPhotosView.as_view(), name="photos"),
    path("<int:pk>/photos/add/", views.AddPhotoView.as_view(), name="add-photo"),
    path("<int:item_pk>/photos/<int:photo_pk>/delete/", views.delete_photo, name="delete-photo"),
    path("<int:item_pk>/photos/<int:photo_pk>/edit/", views.EditPhotoView.as_view(), name="edit-photo"),
]