from django.urls import path

from apps.users.views import register_page, send_code_to_email, register_user, login_page, logout_page
from apps.general.views import home

urlpatterns = [
    path('register/', register_page, name='register_page'),

    path('send_code/', send_code_to_email, name='send_code_to_email'),

    path('register-user/', register_user, name='register_user'),

    path('login-page/', login_page, name='login_page'),

    path('logout-page/', logout_page, name='logout_page'),
]
