from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, FormView
from . import models, forms
from users import models as user_models

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
    
class CreateItemView(FormView):
    
    form_class = forms.CreateItemForm
    template_name = "items/item_create.html"
    
    def form_valid(self, form):
        item = form.save()
        item.owner = self.request.user
        item.save()
        form.save_m2m()
        return redirect(reverse("items:detail", kwargs={'pk': item.pk}))