from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Catagory(models.Model):
    title=models.CharField(max_length=250)
    img=models.ImageField(upload_to='catagoryimg')

    def __str__(self):
        return self.title
    

class Brand(models.Model):
    title=models.CharField(max_length=250)
    img=models.ImageField(upload_to='brandimg')

    def __str__(self):
        return self.title

class Color(models.Model):
    color=models.CharField(max_length=50)
    color_code=models.CharField(max_length=50)

    def __str__(self):
        return self.color

class Size(models.Model):
    size=models.CharField( max_length=50)

    def __str__(self):
        return self.size

class MegaPixel(models.Model):
    mp=models.CharField(max_length=50)
    def __str__(self):
        return self.mp
    

class CcTvProduct(models.Model):
    name=models.CharField(max_length=50)
    mp=models.ForeignKey(MegaPixel, on_delete=models.CASCADE,blank=True, null=True)
    price=models.PositiveIntegerField()
    catagory=models.ForeignKey(Catagory, on_delete=models.CASCADE)
    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)
    color=models.ForeignKey(Color, on_delete=models.CASCADE)
    size=models.ForeignKey(Size, on_delete=models.CASCADE)
    details=models.TextField()
    img=models.ImageField(upload_to='productimg')


    def __str__(self):
        return self.name

class Cart(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey(CcTvProduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)

    @property
    def cart_total(self):
     return self.quantity * self.product.price

class Division(models.Model):
    division=models.CharField(max_length=250)

    def __str__(self):
        return self.division
    


class Customer(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    location=models.CharField( max_length=50)
    distric=models.CharField(max_length=50)
    zipcode=models.CharField( max_length=50)
    division=models.ForeignKey(Division, on_delete=models.CASCADE)
    def __str__(self):
        return self.name
  

Status={
    ('accepted','accepted'),
    ('packed','packed'),
    ('on the way','on the way'),
   ( 'delivered ','delivered')

}



class PlaceOrder(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(CcTvProduct, on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=1)
    order_date= models.DateTimeField(auto_now_add=True)
    status= models.CharField(choices=Status, max_length=50,default='Pending')

    @property
    def cart_total(self):
     return self.quantity * self.product.price
