from django.contrib import admin

from apps.orders.models import OrderCart
from .models import Cart
from apps.general.models import Coupon


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product_feature', 'counts')
    list_display_links = list_display


@admin.register(OrderCart)
class OrderCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_feature', 'counts', 'order')
    list_display_links = list_display


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'code', 'amount', 'amount_is_percent')