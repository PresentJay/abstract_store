from django.core.management.base import BaseCommand
from items.models import Category

class Command(BaseCommand):
    
    help = "This comman creates admenities"
        
    def handle(self, *args, **options):
        category = [          	
            "카테고리-1",
            "카테고리-2",
            "카테고리-3",
            "카테고리-4",
            "카테고리-5",
        ]
        
        for c in category:
            Category.objects.create(category_name=c)
        self.stdout.write(self.style.SUCCESS("Categorys created"))
            