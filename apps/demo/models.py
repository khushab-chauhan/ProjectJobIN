from django.db import models

# Create your models here.

class CAR(models.Model):
    car_name = models.CharField(max_length=255,blank=False,null=False) 
    car_model =models.CharField(max_length=255,blank=False,null=False) 
    car_price = models.FloatField()

    def __str__(self):
        return self.car_name