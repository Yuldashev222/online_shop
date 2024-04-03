from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

from .validators import rating_validate


class Comment(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)
    message = models.CharField(max_length=400)

    user = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, blank=True)

    name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=30, blank=True, null=True)

    rating = models.PositiveSmallIntegerField(validators=[rating_validate], default=0)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.product)