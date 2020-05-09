from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.db import models

# Create your models here.
class User(AbstractUser):
    name = models.CharField(max_length = 10)
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    home_number = PhoneField(blank=True, help_text='Contact home number')
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    