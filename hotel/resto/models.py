from django.db import models


import datetime

class Category(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    slug=models.SlugField(max_length=250,unique=True)
    img=models.ImageField(upload_to="resto/Category",null=True,blank=True)



    def __str__(self):
        return self.name
class Product(models.Model):
    name = models.CharField(max_length=20)
    desc = models.TextField()
    slug = models.SlugField(max_length=250, unique=True)
    img = models.ImageField(upload_to="resto/Category", null=True, blank=True)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    stock=models.DecimalField(max_digits=5,decimal_places=2)

    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name
