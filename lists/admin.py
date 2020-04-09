from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.OrderList)
class OrderListAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Order List Info",
            {
                "fields" : (
                    "status",
                    "user",
                )
            }
        ),
         (
            "Item Info",
            {
                "fields" : (
                    "item",
                    "option",
                    "count",
                    "price",
                )
            }
        ),
    )
    
    list_display = (
        "status",
        "user",
        "item",
    )
    
    list_filter = (
        "status",
        "user",
        "item",
    )