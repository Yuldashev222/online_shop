from django.db import models

from apps.products.models import Product


class Feature(models.Model):
    main_category = models.ForeignKey('categories.MainCategory', on_delete=models.PROTECT,
                                      blank=True, null=True)
    sub_category = models.ForeignKey('categories.SubCategory', on_delete=models.PROTECT,
                                     blank=True, null=True)

    name_uz = models.CharField(max_length=15)
    slug = models.SlugField(max_length=50, unique=True)
    name_ru = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name_uz


class FeatureValue(models.Model):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=1, default=0)
    value = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.feature}: {self.value}"

    class Meta:
        unique_together = ('feature', 'value')


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature_value = models.ForeignKey(FeatureValue, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return str(self.feature_value)

    class Meta:
        unique_together = ('product', 'feature_value')