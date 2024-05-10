from django.db import models

# Create your models here.
class registerDB(models.Model):
    Name = models.CharField(max_length=100,null=True,blank=True)
    Email =models.CharField(max_length=100,null=True,blank=True)
    Password =models.CharField(max_length=100,null=True,blank=True)

class submissionDB(models.Model):
    Task = models.CharField(max_length=100,null=True,blank=True)
    Employee = models.CharField(max_length=100,null=True,blank=True)
    Entry = models.TextField(max_length=500,null=True,blank=True)
