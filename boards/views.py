from django.shortcuts import render
from django.views.generic import ListView
from . import models

# Create your views here.
class ReviewView(ListView):
    model = models.Review
    paginate_by = 10
    paginate_orphans = 5
    # ordering = "created"
    context_object_name = "reviews"
    
class QuestionView(ListView):
    model = models.Question
    paginate_by = 10
    paginate_orphans = 5
    # ordering = "created"
    context_object_name = "questions"
    
class NoticeView(ListView):
    model = models.Notice
    paginate_by = 10
    paginate_orphans = 5
    # ordering = "created"
    context_object_name = "notices"
