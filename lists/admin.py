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
                    "delivery_status",
                    "user",
                )
            }
        ),
         (
            "Item Info",
            {
                "fields" : (
                    "image",
                    "name",
                    "count",
                    "price",
                    "option",
                )
            }
        ),
    )
    
    list_display = (
        "user",
        "delivery_status",
    )
    
    list_filter = (
        "user",
        "delivery_status",
    )
    
    filter_horizontal = (
        "option",
    )
    
@admin.register(models.WishList)
class WishListAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Wish List Info",
            {
                "fields" : (
                    "user",
                    "image",
                    "name",
                    "count",
                    "price",
                    "option",
                )
            }
        ),
    )
    
    list_display = (
        "user",
        "name",
        "count",
        "price",
    )
    
    list_filter = (
        "user",
    )
    
    filter_horizontal = (
        "option",
    )
    
@admin.register(models.ShoppingList)
class ShoppingListAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Shopping List Info",
            {
                "fields" : (
                    "user",
                    "image",
                    "name",
                    "count",
                    "price",
                    "option",
                )
            }
        ),
    )
    
    list_display = (
        "user",
        "name",
        "count",
        "price",
    )
    
    list_filter = (
        "user",
    )
    
    filter_horizontal = (
        "option",
    )