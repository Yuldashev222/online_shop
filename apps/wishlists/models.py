from django.db import models


class WishList(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.product)