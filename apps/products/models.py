from django.db import models

from django.core.validators import MinValueValidator


class Product(models.Model):
    title_uz = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True)
    title_ru = models.CharField(max_length=30, blank=True)
    price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    old_price = models.DecimalField(max_digits=20, decimal_places=2, validators=[MinValueValidator(0)])
    short_desc_uz = models.CharField(max_length=300)
    short_desc_ru = models.CharField(max_length=300, blank=True)
    long_desc_uz = models.TextField(max_length=1500)
    long_desc_ru = models.TextField(max_length=1500, blank=True)
    review_counts = models.PositiveIntegerField(default=0)
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz
