from django.contrib import admin

from .models import Product
from apps.features.models import ProductFeature


class ProductFeatureInline(admin.StackedInline):
    model = ProductFeature


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'title_ru', 'slug', 'price', 'old_price', 'short_desc_uz',
                    'short_desc_ru', 'long_desc_uz', 'long_desc_ru', 'review_counts', 'rating')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title_uz']}
    inlines = [ProductFeatureInline]