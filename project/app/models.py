from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Client(AbstractUser):
    birth_date = models.DateField(auto_now=False,blank=False,null=False)
    
    def __str__(self):
        return self.username