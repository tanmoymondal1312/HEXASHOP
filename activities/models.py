from django.db import models
from accounts.models import CustomUser

# Create your models here.
class Activities(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  
    data = models.TextField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Activities by {self.user.username} "