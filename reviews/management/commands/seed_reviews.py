import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews.models import Review
from users import models as user_models
from items import models as item_models

class Command(BaseCommand):
    
    help = "This comman creates many reviews"
    
    def add_arguments(self, parser):
        parser.add_argument(
            "--number", default=2, type=int, help = "How many reviews do you want to create"
        )
        
    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_items = item_models.Item.objects.all()
        
        seeder.add_entity(Review, number, {
            "user": lambda x: random.choice(all_users),
            "item": lambda x: random.choice(all_items),
        })
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!!"))
            