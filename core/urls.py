from django.urls import path
from boards import views as boards_views

app_name = "core"

urlpatterns = [
    path('Review', boards_views.ReviewView.as_view(), name='Review'),
    path('Question', boards_views.QuestionView.as_view(), name='Question'),
    path('Notice', boards_views.NoticeView.as_view(), name='Notice'),
]
