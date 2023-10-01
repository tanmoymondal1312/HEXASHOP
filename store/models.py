from django.db import models
from category.models import Category
from accounts.models import CustomUser
from seller.models import Seller
from django.db.models import Avg


class Product(models.Model):
    SIZE_CHOICES = (
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
        ('XXXL', 'XXXL'),
        
    )
    
    COLOR_CHOICES =(
       ('Red', 'Red'),
       ('White','White'),
       ('Blue', 'Blue'),
       ('Green', 'Green'),
       ('Yellow', 'Yellow'),
       ('Black', 'Black'),
       ('Vilolet', 'Violet'),
    )
    
    created_by = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller_products', null=True, blank=True)
    product_name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sizes = models.CharField(max_length=5, choices=SIZE_CHOICES, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    color = models.CharField(max_length=20, choices= COLOR_CHOICES, blank=True)


class Reviews(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    product = models.ForeignKey(Product, on_delete=models.CASCADE) 
    rating = models.PositiveIntegerField(default=5) 
    comment = models.TextField(max_length=1000) 
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Review by {self.user.username} for {self.product.product_name}"
