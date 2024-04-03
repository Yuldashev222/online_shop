from django.contrib import admin

from .models import WishList


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'created_at')
    list_display_links = list_display
