from django.contrib import admin
from . import models
from photos import admin as phtos_admin

# Register your models here.
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines= (phtos_admin.PhotoInline,)
    
    fieldsets = (
        (
            "Product Info",
            {
                "fields" : (
                    "name",
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
