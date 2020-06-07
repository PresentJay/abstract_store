from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView, FormView, UpdateView
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
        return redirect(reverse("items:photos", kwargs={'pk': item.pk}))
    
class EditItemView(UpdateView):
    
    model = models.Item
    template_name = "items/item_edit.html"
    fields = (
        "name",
        "shorten_description",
        "tag",
        "category",
        "status",
        "price",
        "description",
        "count",
    )
    
    def get_success_url(self):
        item_pk = self.kwargs.get("pk")
        return reverse("items:detail", kwargs={"pk":item_pk})
    
class ItemPhotosView(DetailView):
    
    model = models.Item
    template_name = "items/item_phtos.html"
    
    def get_object(self, queryset=None):
        item = super().get_object(queryset=queryset)
        if item.owner.pk != self.request.user.pk:
            raise Http404()
        return item

class AddPhotoView(FormView):
    
    template_name = "items/photo_create.html"
    form_class = forms.CreatePhotoForm
    
    def form_valid(self, form):
        pk = self.kwargs.get('pk')
        form.save(pk)
        # messages.success(self.request, "Photo Uploaded")
        return redirect(reverse("items:photos", kwargs={'pk':pk}))
    
@login_required  
def delete_photo(request, item_pk, photo_pk):
    user = request.user
    try:
        item = models.Item.objects.get(pk=item_pk)
        if item.owner.pk != user.pk:
            # messages.error(request, "Can't delete that photo")
            print("Can't delete that photo")
        else:
            models.Photo.objects.filter(pk=photo_pk).delete()
            # messages.success(request, "Photo Deleted")
            print("Photo Deleted")
        return redirect(reverse("items:photos", kwargs={'pk':item_pk}))
    except models.Item.DoesNotExist:
        return redirect(reverse("core:home"))
    
class EditPhotoView(UpdateView):
    
    model = models.Photo
    template_name = "items/photo_edit.html"
    pk_url_kwarg = "photo_pk"
    success_message = "Photo Updated"
    fields = ("file",)
    
    def get_success_url(self):
        item_pk = self.kwargs.get("item_pk")
        return reverse("items:photos", kwargs={"pk":item_pk})
