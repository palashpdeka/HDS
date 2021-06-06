from django.db import models
from django.contrib.auth.models import User,Group

class product(models.Model):
    name=models.CharField(max_length=100)
    pic=models.ImageField(upload_to='media')
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    description=models.CharField(max_length=10000)
    def __str__(self):
        return self.name

class order(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    item=models.CharField(max_length=100)#pro=product
    quantity=models.IntegerField()
    price=models.IntegerField()
    status=models.IntegerField(default=0) #0-on bag, 1-ordered, 2-out for delivery, 3-delivered, 4-cancelled
    date=models.DateTimeField(auto_now_add=True, blank=True)

class customer(models.Model):
    user=models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    address=models.CharField(max_length=10000)
    phn=models.CharField(max_length=20)
    #current=models.ManyToManyField(order) #current_orders
    #past=models.ManyToManyField(bag) ##past_orders

