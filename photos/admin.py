from django.contrib import admin
from django.utils.html import mark_safe
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo

@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Photo Info",
            {
                "fields" : (
                    "caption",
                    "file"
                )
            }
        ),
        (
            "Additional Info",
            {
                "fields" : (
                    "item",
                    "review",
                    "question",
                    "notice",
                    "answer"
                )
            }
        ),
    )
    
    list_display = (
        "__str__",
        "get_thumnnail"
    )
    
    def get_thumnnail(self, obj):
        return mark_safe(f'<img width="50px" src="{obj.file.url}"/>')
    get_thumnnail.short_description = "Thumnnail"