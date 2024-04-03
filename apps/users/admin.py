from django.contrib import admin

from .models import CustomUser, UserAuthCode


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name',
                    'email', 'phone_number', 'address1', 'address2',
                    'country', 'region', 'district', 'zip_code')


admin.site.register(UserAuthCode)

# CustomUser.objects.create(
#         email='email1@asd.asd',
#         first_name='first_name',
#         last_name='last_name',
#         phone_number='+998999849842',
#         password='998999849842'
# )
