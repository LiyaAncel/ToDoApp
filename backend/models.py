from django.db import models

# Create your models here.
class taskDB(models.Model):
    Task_Title = models.CharField(max_length=100,null=True,blank=True)
    Employee = models.CharField(max_length=100,null=True,blank=True)
    Description = models.TextField(max_length=500,null=True,blank=True)
    Due_date= models.DateField(null=True)

class reportDB(models.Model):
    Task_Title = models.CharField(max_length=100, null=True, blank=True)
    Employee = models.CharField(max_length=100, null=True, blank=True)
    Result = models.CharField(max_length=100, null=True, blank=True)
