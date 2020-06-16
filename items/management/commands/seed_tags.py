from django.core.management.base import BaseCommand
from items.models import Tag

class Command(BaseCommand):
    
    help = "This comman creates tags"
        
    def handle(self, *args, **options):
        tags = [          	
            "태그-1",
            "태그-2",
            "태그-3",
            "태그-4",
            "태그-5",
        ]
        
        for t in tags:
            Tag.objects.create(tag_name=t)
        self.stdout.write(self.style.SUCCESS("Tags created"))
            