from django.db import models
from resto.models import Product
from django.contrib.auth.models import User
from datetime import datetime
class Cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    products=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField()
    date_added=models.DateTimeField(auto_now_add=True)
    active=models.BooleanField(default=True)
    def subtotal(self):
        return self.quantity*self.products.price
    def __str__(self):
        return self.products.name
class Account(models.Model):
    acctnumber=models.CharField(max_length=200)
    accttype=models.CharField(max_length=30)
    amount=models.IntegerField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.acctnumber
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)
    address = models.TextField()
    phone = models.CharField(max_length=11)
    order_status = models.CharField(max_length=30, default="pending")
    delivery_status = models.CharField(max_length=30, default="pending")
    noofitems = models.IntegerField()
    date_added = models.DateTimeField(auto_now_add=True)
    pickup_time=models.CharField(max_length=6)
    pickup_status = models.CharField(max_length=30, default="pending")
    pickup_date=models.DateTimeField(default=datetime(2023, 6, 30, 22, 30, 0))
    def __str__(self):
        return self.user.username

    def subtotal1(self):
        return self.noofitems*self.products.price

