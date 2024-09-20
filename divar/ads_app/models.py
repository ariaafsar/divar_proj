from django.db import models
from user_app.models import UserAccount
from django.core.validators import MinValueValidator

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Ad(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.PositiveBigIntegerField()
    location = models.CharField(max_length=255)
    category = models.ForeignKey(Category , on_delete=models.CASCADE)
    user = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.title






# Create your models here.
