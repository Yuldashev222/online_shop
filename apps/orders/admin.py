from django.contrib import admin

from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'payment_method', 'payment_method_name', 'total_price', 'coupon_price', 'delivery',
                    'is_paid', 'first_name', 'last_name', 'email', 'phone_number', 'address1',
                    'address2', 'country', 'region', 'district', 'zip_code')
    list_display_links = list_display
