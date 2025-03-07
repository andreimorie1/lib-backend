from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    date_joined = models.DateTimeField(auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    release = models.DateField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=7)
    genre = models.CharField(max_length=300)
    
