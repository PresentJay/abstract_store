from django.contrib import admin
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines= (
        PhotoInline,
    )
    
    fieldsets = (
        (
            "Review Info",
            {
                "fields" : (
                    "title",
                    "content",
                    "user",
                    "item",
                )
            }
        ),
    )
    
    list_display = (
        "title",
        "content",
        "user",
        "item",
    )
    
    list_filter = (
        "user",
    )
    
@admin.register(models.Recomment)
class RecommentAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Recomment Info",
            {
                "fields" : (
                    "title",
                    "content",
                    "user",
                    "review",
                )
            }
        ),
    )
    
    list_display = (
        "title",
        "content",
        "user",
        "review",
    )
    
    list_filter = (
        "user",
        "review",
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
                    "review",
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