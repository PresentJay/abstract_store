from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.db import models
from core import models as core_models

# Create your models here.


class User(AbstractUser):
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    name = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    postal_code = models.CharField(max_length=7, blank=True)
    birthdate = models.DateField(null=True)

    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    home_number = PhoneField(blank=True, help_text='Contact home number')
    phone_number = PhoneField(blank=True, help_text='Contact phone number')

class FavList(core_models.TimeStampedModel):
    
    user = models.OneToOneField("users.User",related_name="lists" , on_delete=models.CASCADE)
    items = models.ManyToManyField("items.Item",related_name="lists" , blank=True)
    
    def __str__(self):
        return self.user.name