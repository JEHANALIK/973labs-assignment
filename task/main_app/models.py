from django.db import models
from django.db.models import Model

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    pic = models.ImageField(upload_to ='main_app/static/uploads/', blank=True)

class Customers(models.Model):
    username= models.CharField(max_length=100)
    description= models.TextField(max_length=265)
    path= models.CharField(max_length=100)
    action= models.CharField(max_length=100)
    error= models.CharField(max_length=100)
    client= models.ForeignKey(Client, on_delete=models.CASCADE)

   
