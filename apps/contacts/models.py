from django.db import models

from apps.users.models import CustomUser


class Contact(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)

    name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=90, blank=True, null=True)

    title = models.CharField(max_length=90)
    message = models.TextField(max_length=1500)

    def __str__(self):
        return self.name