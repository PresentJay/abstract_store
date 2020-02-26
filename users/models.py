from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.db import models

# Create your models here.


class User(AbstractUser):
<<<<<<< HEAD

    name = models.CharField(max_length=10)
=======
    name = models.CharField(max_length = 10)
>>>>>>> 6a930a4cbb0dcf4f43e807d9787fec0223e225e6
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    home_number = PhoneField(blank=True, help_text='Contact home number')
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
