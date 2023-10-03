from django.db import models
from store.models import Product
from accounts.models import CustomUser
from django.core.validators import MaxValueValidator

# Create your models here.
class Ratting(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField(default=5, validators=[MaxValueValidator(5)])
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Rating by {self.user.username} for {self.product.product_name}"

    
class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Comment by {self.user.username} for {self.product.product_name}"