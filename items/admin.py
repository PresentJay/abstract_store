from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo
    
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines= (
        PhotoInline,
    )
    
    fieldsets = (
        (
            "Item Info",
            {
                "fields" : (
                    "name",
                    "shorten_description",
                    "tag",
                    "category",
                    "status",
                    "price",
                    "description",
                    "count",
                    "owner",
                )
            }
        ),
    )
    
    list_display = (
        "name",
        "status",
        "owner",
    )
    
    list_filter = (
        "name",
        "status",
        "owner",
        "tag",
        "category",
        "price",
        "status",
    )
    
    filter_horizontal = (
        "tag",
        "category",
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
                    "name",
                    "extra_money",
                    "item",
                )
            }
        ),
    )
    
    list_display = (
        "name",
        "extra_money",
        "item",
    )

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Category Info",
            {
                "fields" : (
                    "category_name",
                )
            }
        ),
    )
    
    list_display = (
        "category_name",
    )

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Photo Info",
            {
                "fields" : (
                    "file",
                )
            }
        ),
        (
            "Related Info",
            {
                "fields" : (
                    "item",
                )
            }
        ),
    )
    
    list_display = (
        "get_photo",
    )
    
    def get_photo(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
    get_photo.short_description = "Photo"