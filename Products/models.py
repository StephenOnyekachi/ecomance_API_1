
from django.db import models
from Accounts.models import Users

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    discount = models.IntegerField(null=True)
    is_discount = models.BooleanField(default=False)
    is_avaliable = models.BooleanField(default=True)
    description = models.TextField()
    file = models.FileField(upload_to='file', null=True)

    def __str__(self):
        return self.name
    

class Cart(models.Model):
    customer = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='cart_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_product')
    quantity = models.IntegerField()
    price = models.IntegerField()
    added = models.DateTimeField(auto_created=True, auto_now=True)
    paid = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    date_paid = models.DateTimeField()

    def __str__(self):
        return self.customer.usernaame
    

    