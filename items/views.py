from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . import models

# Create your views here.
class HomeView(ListView):
    
    model = models.Item
    paginate_by = 12
    paginate_orphans = 5
    ordering = "created"
    context_object_name = "items"
    
class ItemDetail(DetailView):
    
    model = models.Item
    context_object_name = "item"