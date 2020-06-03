from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from django.db import models

# Create your models here.


class User(AbstractUser):
<<<<<<< HEAD
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, "Male"),
        (GENDER_FEMALE, "Female"),
    )

    name = models.CharField(max_length=10)
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
=======

    name = models.CharField(max_length=10)
>>>>>>> adjusting branches
    address1 = models.CharField(max_length=1024)
    address2 = models.CharField(max_length=1024)
    birthdate = models.DateField(null=True)

    email_confirmed = models.BooleanField(default=False)
    email_secret = models.CharField(max_length=20, default="", blank=True)

    home_number = PhoneField(blank=True, help_text='Contact home number')
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
