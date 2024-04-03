from django.db import models
from django.core.exceptions import ValidationError

from .validators import phone_validate
from apps.categories.models import SubCategory


class SocialLink(models.Model):
    icon = models.ImageField(upload_to='general/icon')
    name = models.CharField(max_length=60)
    slug = models.SlugField(max_length=50, unique=True)
    link = models.URLField()

    def __str__(self):
        return self.name


class PaymentMethod(models.Model):
    name = models.CharField(max_length=35)
    slug = models.SlugField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class General(models.Model):
    delivery_price = models.PositiveIntegerField(help_text='So`mda kiriting!')
    store_name = models.CharField(max_length=30)
    logo = models.ImageField(upload_to='image/%Y/%m/%d/')
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    email = models.EmailField()
    address_uz = models.CharField(max_length=40)
    address_ru = models.CharField(max_length=40, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    desc_uz = models.TextField(max_length=1400)
    desc_ru = models.TextField(max_length=1400, blank=True)

    def __str__(self):
        return self.email


class Service(models.Model):
    title_uz = models.CharField(max_length=20)
    title_ru = models.CharField(max_length=20)
    slug = models.SlugField(max_length=50, unique=True)
    icon = models.ImageField(upload_to='services/icons/%Y/%m/%d/')

    def __str__(self):
        return self.title_uz


class Branch(models.Model):
    image = models.ImageField(upload_to='general/image')
    title = models.CharField(max_length=35)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.title


class Banner(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE)

    store_name = models.CharField(max_length=20)
    title_uz = models.CharField(max_length=30)
    title_ru = models.CharField(max_length=30, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    desc_uz = models.TextField(max_length=100)
    desc_ru = models.TextField(max_length=100, blank=True)

    def __str__(self):
        return self.title_uz


class Coupon(models.Model):
    title = models.CharField(max_length=10)
    code = models.CharField(max_length=10, unique=True)
    amount = models.DecimalField(max_digits=10, decimal_places=1, help_text='So`mda yoki foizda kiriting!')
    amount_is_percent = models.BooleanField(default=True)

    def clean(self):
        if self.amount_is_percent and not (1 <= self.amount <= 100):
            raise ValidationError({'amount': 'invalid amount [1, 100]'})

    def __str__(self):
        return self.title