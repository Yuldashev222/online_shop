from django.contrib import admin

from .models import Feature, FeatureValue, ProductFeature
from apps.products.models import Product


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_category', 'sub_category', 'slug', 'name_uz', 'name_ru')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name_uz']}


@admin.register(FeatureValue)
class FeatureValueAdmin(admin.ModelAdmin):
    list_display = ('id', 'feature', 'value', 'price')
    list_display_links = list_display


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'feature_value', 'quantity')
    list_display_links = list_display

