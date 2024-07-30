from django.db import models

# Create your models here.
  

class Customer(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True) 
    Email=models.EmailField(null=True,blank=True) 
    Address=models.CharField(max_length=100,null=True,blank=True)
    Image=models.FileField(null=True,blank=True)
    Username=models.CharField(max_length=100,null=True,blank=True,unique=True)
    Password=models.CharField(max_length=100,null=True,blank=True)


    def __str__(self):
        return self.Name

