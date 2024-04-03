from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.general.models import phone_validate
from apps.users.managers import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    objects = CustomUserManager()

    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)

    phone_number = models.CharField(max_length=13, validators=[phone_validate], blank=True)
    address1 = models.CharField(max_length=90, blank=True)
    address2 = models.CharField(max_length=90, blank=True)
    country = models.CharField(max_length=80, blank=True)
    region = models.CharField(max_length=80, blank=True)
    district = models.CharField(max_length=80, blank=True)
    zip_code = models.CharField(max_length=15, blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return str(self.get_full_name())

    class Meta:
        ordering = ['-pk']


class UserAuthCode(models.Model):
    email = models.EmailField()
    code = models.CharField(max_length=4)

    expire_at = models.DateTimeField(null=True)
