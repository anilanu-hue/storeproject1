from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from spencersapp.models import Products


class Orders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    purchase_id=models.CharField(max_length=30)
    is_order=models.BooleanField(max_length=10,default=False)
    total=models.FloatField(default=0.0)
    order_status=models.CharField(max_length=20,default="Pending")
    ordered_on=models.DateTimeField(auto_now_add=True,null=True,blank=True)
    shipping_to = models.TextField(null=True, blank=True, default='hyderabad')



class CartOrders(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product = models.ForeignKey(Products,on_delete=models.CASCADE)
    order_id=models.ForeignKey(Orders,on_delete=models.CASCADE,null=True,blank=True)
    quantity=models.IntegerField()
    price=models.FloatField()
    corier_name=models.CharField(max_length=50,null=True,blank=True)
    payment_type=models.CharField(max_length=50,null=True,blank=True)
    isdeleted = models.BooleanField(max_length=10,default=False)
    added_on = models.DateTimeField(auto_now_add=True)
    added_by = models.IntegerField()
    #is_order=models.BooleanField(max_length=10,default=False)