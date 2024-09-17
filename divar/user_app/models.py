from django.db import models
from django.contrib.auth.models import User

class UserAccount(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username
# Create your models here.
