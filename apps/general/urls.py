from django.urls import path
from apps.general.views import home


urlpatterns = [
    path('', home, name='home-page'),
]