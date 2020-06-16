import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from users import models as user_models
from items import models as item_models

class Command(BaseCommand):
    
    help = "This comman creates many favs"
        
    def handle(self, *args, **options):
        all_users = user_models.User.objects.all()
        all_items = item_models.Item.objects.all()
        for User in all_users:
            fav = user_models.FavList.objects.create(user=User)
            for item in all_items:
                magic_number = random.randint(0,15)
                if magic_number % 2 == 0:
                    fav.items.add(item)
        self.stdout.write(self.style.SUCCESS("favs created!!"))
            