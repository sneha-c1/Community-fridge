from django.db import models

# Create your models here.
class Users(models.Model):
    Name=models.CharField(max_length=30)
    EmailID=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    Phone=models.BigIntegerField()
    Address=models.TextField()
    Place=models.CharField(max_length=30)
class donation(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('declined', 'Declined'),
    ]
    Name=models.CharField(max_length=30)
    Type_of_donation=models.CharField(max_length=30)
    Item=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=30)
    Description=models.TextField()
    Location=models.CharField(max_length=30)
    Contact_no=models.CharField(max_length=30)
    Pic=models.ImageField(upload_to='static/images/donation/')
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending')
class foods(models.Model):
    Name=models.CharField(max_length=30)
    Item=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=30)
    Description=models.TextField()
    Location=models.CharField(max_length=30)
    Contact_no=models.CharField(max_length=30)
    Pic=models.ImageField(upload_to='static/images/donation/foods/')
class clothes(models.Model):
    Name=models.CharField(max_length=30)
    Item=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=30)
    Description=models.TextField()
    Location=models.CharField(max_length=30)
    Contact_no=models.CharField(max_length=30)
    Pic=models.ImageField(upload_to='static/images/donation/clothes/')
class requestitem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accept', 'accept'),
        ('reject', 'reject'),
    ]
    Email=models.CharField(max_length=30)
    ItemType=models.CharField(max_length=30)
    ItemName=models.CharField(max_length=30)
    Quantity=models.CharField(max_length=30)
    Location=models.CharField(max_length=30)
    PhoneNumber=models.BigIntegerField()
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending')
class DriverLoginDetails(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('delivered', 'Delivered'),
        ('on the way', 'On the way'),
    ]
    Email=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    PlaceAllocation=models.CharField(max_length=30)
    Status=models.CharField(max_length=30,choices=STATUS_CHOICES, default='pending')