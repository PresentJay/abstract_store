from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.views.generic import FormView, TemplateView
from django.urls import reverse_lazy
from . import forms, models
from items import models as item_models

# Create your views here.


class LoginView(FormView):

    template_name = "users/login.html"
    form_class = forms.LoginForm

    def form_valid(self, form):
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)
        if user is not None:
            login(self.request, user)
        return super().form_valid(form)

    def get_success_url(self):
        next_arg = self.request.GET.get("next")
        if next_arg is not None:
            return next_arg
        else:
            return reverse("core:home")


def log_out(request):
    logout(request)
    return redirect(reverse("core:home"))


class SignUpView(FormView):
    template_name = "users/signup.html"
    form_class = forms.SignUpForm
    success_url = reverse_lazy("core:home")

    def form_valid(self, form):
        form.save()
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(self.request, username=email, password=password)

        if user is not None:
            login(self.request, user)

        return super().form_valid(form)

def add_fav(request, item_pk):
    item = item_models.Item.objects.get_or_none(pk=item_pk)
    if item is not None:
        the_list, _ = models.FavList.objects.get_or_create(user=request.user)
        the_list.items.add(item)
    return redirect(reverse("items:detail", kwargs={"pk":item_pk}))
    
class SeeFavsView(TemplateView):
    template_name = "users/favlist_list.html"