from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Product Info",
            {
                "fields" : (
                    "name",
                    "image",
                    "description",
                    "price",
                    "product",
                    "status",
                    "tag",
                    "option",
                )
            }
        ),
    )
    
    list_display = (
        "name",
        "image",
        "description",
        "price",
        "product",
        "status",
    )
    
    list_filter = (
        "tag",
    )
    
    filter_horizontal = (
        "tag",
        "option",
    )

@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Tag Info",
            {
                "fields" : (
                    "tag_name",
                )
            }
        ),
    )
    
@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Option Info",
            {
                "fields" : (
                    "option_name",
                    "extra_money",
                )
            }
        ),
    )
    
    list_display = (
        "option_name",
        "extra_money",
    )
