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