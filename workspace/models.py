from django.db import models
from store.models import Product
from seller.models import Seller
import datetime


class SelleProduct(models.Model):
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.datetime(2023, 10, 10, 12, 0, 0))

    # modified_at = models.DateTimeField(auto_now=True)