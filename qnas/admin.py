from django.contrib import admin
from . import models

# Register your models here.
class PhotoInline(admin.TabularInline):
    model = models.Photo
    
@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines= (
        PhotoInline,
    )
    
    fieldsets = (
        (
            "Question Info",
            {
                "fields" : (
                    "answer_status",
                    "title",
                    "content",
                    "user",
                    "item",
                )
            }
        ),
    )
    
    list_display = (
        "answer_status",
        "title",
        "content",
        "user",
        "item",
    )
    
    list_filter = (
        "answer_status",
        "user",
        "item",
    )
    
@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    fieldsets = (
        (
            "Answer Info",
            {
                "fields" : (
                    "title",
                    "content",
                    "user",
                )
            }
        ),
        (
            "Info",
            {
                "fields" : (
                    "question",
                )
            }
        ),
    )
    
    list_display = (
        "title",
        "content",
        "user",
    )
    
    list_filter = (
        "user",
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
                    "question",
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