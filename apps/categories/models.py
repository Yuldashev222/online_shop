from django.db import models
from django.core.validators import FileExtensionValidator


class MainCategory(models.Model):
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=True)
    image = models.ImageField(upload_to='categories/image')
    product_counts = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.name_uz


class SubCategory(models.Model):
    main_category = models.ForeignKey(MainCategory, on_delete=models.PROTECT)
    name_uz = models.CharField(max_length=50)
    name_ru = models.CharField(max_length=50, blank=True)
    slug = models.SlugField(max_length=50, unique=True)

    def __str__(self):
        return self.name_uz

