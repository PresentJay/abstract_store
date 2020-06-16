from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Order Info",
            {
                "fields" : (
                    "user",
                    "items",
                    "state",
                    "receipt_id",
                    "address",
                    "postal_code",
                    "confirmed_date",
                    "shipping_started_date",
                    "completed_date",
                )
            }
        ),
    )
    
    list_display = (
        "__str__",
        "state",
        "user",
        "confirmed_date",
        "shipping_started_date",
        "completed_date",
    )
    
    list_filter = (
        "state",
        "user",
    )

@admin.register(models.OrderingItem)
class OrderingItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "OrderingItem Info",
            {
                "fields" : (
                    "item",
                    "option",
                    "quantity",
                )
            }
        ),
    )
    
    list_display = (
        "item",
        "quantity",
    )
    
    list_filter = (
        "item",
    )