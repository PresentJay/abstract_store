from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User) #decorator
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (
            "Detail Info",
            {
                "fields" : (
                    "name",
                    "address1",
                    "address2",
                    "home_number",
                    "phone_number",
                )
            }
        ),
    )
    
    list_display = (
        "username",
        "email",
        "is_staff"
    )
    
@admin.register(models.FavList)
class FavListAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Favourite List Info",
            {
                "fields" : (
                    "user",
                    "items",
                )
            }
        ),
    )
    
    list_display = (
        "user",
    )
    
    list_filter = (
        "user",
    )
    
    filter_horizontal = (
        "items",
    )