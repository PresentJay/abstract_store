from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo
    
class ThumbnailInline(admin.TabularInline):
    model = models.Thumbnail
    
@admin.register(models.Item)
class ItemAdmin(admin.ModelAdmin):
    inlines= (
        ThumbnailInline,
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
                    "option",
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
        "option",
        "price",
        "status",
    )
    
    filter_horizontal = (
        "tag",
        "category",
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
    
@admin.register(models.Thumbnail)
class ThumbnailAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Thumbnail Info",
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
        "get_thumbnail",
    )
    
    def get_thumbnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
    get_thumbnail.short_description = "Thumbnail"