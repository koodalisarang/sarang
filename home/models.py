from django.db import models

# Create your models here.
class register(models.Model):
    username= models.CharField(max_length=50)
    email=models.EmailField()
    password=models.CharField(max_length=10)
    phone=models.IntegerField()
    address=models.CharField(max_length=100)

