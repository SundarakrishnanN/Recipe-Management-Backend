from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  
    name=models.CharField(max_length=100,null=False)
    phone_number = models.CharField(max_length=10, blank=True, null=True)

    USERNAME_FIELD = 'email' 
    REQUIRED_FIELDS = ['username'] 

    def __str__(self):
        return self.email
