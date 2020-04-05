from django.db import models
from django import forms

class Category(models.Model):

    name = models.CharField(max_length=250)
    def __str__(self):
        return self.name
        
class BatteryDataSet(models.Model):
    serial_no         = models.TextField(max_length=150, default="")
    time              = models.TextField(max_length=150, default="") 
    charging_level    = models.CharField(max_length=100)
    temperature       = models.CharField(max_length=150)
    battery_voltage   = models.CharField(max_length=150)

    decreased_voltage = models.TextField(max_length=150)
    charging_status   = models.CharField(max_length=150)
   
    def __str__(self):
        return self.time

class Result(models.Model):
    imei               = models.TextField(max_length=150, default="")
    result             = models.TextField(max_length=150, default="")
     
    model = models.ForeignKey(
        'Category',
        on_delete = models.CASCADE
    )   
    def __str__(self):
        return self.imei        

  


