from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicle(models.Model):

    Vehicle_id = models.CharField(max_length=8, unique=True)
    Capacity = models.IntegerField()
    Type = models.CharField(max_length=20)
    refrigerated = models.BooleanField()



class Payment(models.Model):
    cardholder = models.CharField(max_length=100)
    card_number = models.CharField(max_length=16)
    expiry_date = models.DateField()
    cvc = models.CharField(max_length=3)
    Vehicle_id = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE, default=user.id)  

    def __str__(self):
        return f"Payment for Vehicle {self.Vehicle_id} - ${self.amount}"



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    vehicle_returned = models.BooleanField(default=False)


class Book(models.Model):
    product = models.CharField(max_length=100)
    perishable = models.BooleanField(default=False)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    pickup = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
   
    