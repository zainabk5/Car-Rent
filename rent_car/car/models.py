from django.db import models
from tinymce.models import HTMLField
from PIL import Image
from django.contrib.auth.models import AbstractUser

class User(models.Model):
    username = models.CharField(max_length=100)
    useremail = models.EmailField()
    userphone = models.CharField(max_length=100)
    userpassword = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username}" 

class Brand(models.Model):
    brand_name = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.brand_name}" 

class Vehicle(models.Model):
    car_name= models.CharField(max_length=100)
    car_image = models.ImageField(upload_to='static/')
    car_price=models.IntegerField()
    car_des = models.TextField()
    brand=models.ForeignKey(Brand,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.car_name}" 

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone= models.CharField(max_length=100)
    des = models.TextField(default='true')

class Booking(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    date = models.DateField(default='true')
    status = models.BooleanField(default=False)

class Testimonial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    client_image = models.ImageField(upload_to='static/')
    client_name = models.CharField(max_length=100)
    client_des = models.TextField(default='true')
    status = models.BooleanField(default=False)
    

class Admin_user(models.Model):
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField()
    admin_phone= models.CharField(max_length=100)
    admin_password = models.CharField(max_length=100)
