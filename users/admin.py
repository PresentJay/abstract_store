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