from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(User , null=True , on_delete=models.CASCADE)
    name = models.CharField(max_length=50 , null=True)
    email = models.EmailField(max_length = 50 , null=True)

    def __str__(self):
        return self.name



class Products(models.Model):
    name= models.CharField(max_length=100 , null=False)
    price = models.IntegerField(default=0 )
    desc = models.TextField()

    def __str__(self):
        return self.name 

class Order(models.Model):
    user = models.ForeignKey(Customer , on_delete = models.CASCADE , null=True)
    complete = models.BooleanField(default=False )
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.name

class OrderItem(models.Model):
    product = models.ForeignKey(Products , null=True , on_delete = models.CASCADE)
    order = models.ForeignKey(Order , on_delete= models.CASCADE)
    quantity = models.IntegerField(default=0 , null=True , blank=True)

    def __str__(self):
        return self.product.name 

