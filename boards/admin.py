from django.contrib import admin
from . import models
from photos import admin as phtos_admin

# Register your models here.
@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    inlines= (phtos_admin.PhotoInline,)

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines= (phtos_admin.PhotoInline,)

@admin.register(models.Notice)
class NoticeAdmin(admin.ModelAdmin):
    inlines= (phtos_admin.PhotoInline,)

@admin.register(models.Answer)
class AnswerAdmin(admin.ModelAdmin):
    inlines= (phtos_admin.PhotoInline,)