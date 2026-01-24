from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import TextField
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar/', null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=False,unique=True)
    data_birthday = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)