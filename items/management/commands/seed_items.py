import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed
from items.models import Option
from items import models as item_models
from users import models as user_models

class Command(BaseCommand):
    
    help = "This comman creates many items"
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help = "How many items do you want to create"
        )
        
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        
        options = [          	
            "옵션-1",
            "옵션-2",
            "옵션-3",
            ]
        
        seeder.add_entity(item_models.Item, number,{
            "price": lambda x: random.randint(100000,100000000),
            "count": lambda x: random.randint(1,1000),
            "owner": lambda x: random.choice(all_users),
        },)
        creadted_photos = seeder.execute()
        creadted_clean = flatten(list(creadted_photos.values()))
        
        categorys = item_models.Category.objects.all()
        tags = item_models.Tag.objects.all()
        
        for pk in creadted_clean:
            item = item_models.Item.objects.get(pk=pk)
            for i in range(3, random.randint(10,30)):
                item_models.Photo.objects.create(
                    file=f"/item_photos_seed/{random.randint(1,9)}.jpg",
                    item=item,
                )
            for c in categorys:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    item.category.add(c)
            for t in tags:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    item.tag.add(t)
            
            for o in options:
                option = Option.objects.create(
                    name=o,
                    extra_money=random.randint(1000,100000),
                    item=item
                    )
                    
        self.stdout.write(self.style.SUCCESS(f"{number} items created!!"))