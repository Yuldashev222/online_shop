from django.db import models
from django.core.validators import MinValueValidator

from apps.features.models import ProductFeature


class Cart(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)

    product_feature = models.ForeignKey(ProductFeature, on_delete=models.CASCADE)
    counts = models.PositiveSmallIntegerField(validators=[MinValueValidator(1)])

    def __str__(self):
        return str(self.product_feature)


