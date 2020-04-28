from django import forms
from . import models

class CreateItemForm(forms.ModelForm):
    class Meta:
        model = models.Item
        fields=(
            "name",
            "shorten_description",
            "tag",
            "category",
            "status",
            "price",
            "description",
            "count",
        )
        
    def save(self, *args, **kwargs):
        item = super().save(commit=False)
        return item
    
    