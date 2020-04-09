from django.urls import path
from . import views

app_name = "qnas"

urlpatterns = [
    path("qna", views.QnaView.as_view(), name="qna"),
]
