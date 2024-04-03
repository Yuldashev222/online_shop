from django.contrib import admin

from .models import SocialLink, PaymentMethod, General, Service, Branch


@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'icon', 'name', 'slug', 'link')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['name']}


@admin.register(PaymentMethod)
class PaymentMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['slug']}


@admin.register(General)
class GeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'delivery_price', 'logo', 'phone_number',
                    'email', 'address_uz', 'address_ru', 'longitude',
                    'latitude', 'desc_uz', 'desc_ru')

    def has_add_permission(self, request):
        return not General.objects.exists()


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title_uz', 'title_ru', 'slug', 'icon')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title_uz']}


@admin.register(Branch)
class BranchAdmin(admin.ModelAdmin):
    list_display = ('id', 'image', 'title', 'slug')
    list_display_links = list_display
    prepopulated_fields = {'slug': ['title']}
