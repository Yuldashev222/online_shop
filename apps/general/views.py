from django.shortcuts import render

from apps.general.models import General


def home(request):
    store_data = General.objects.first()
    ctx = {
        'store_data': store_data
    }
    return render(request, 'index.html', ctx)