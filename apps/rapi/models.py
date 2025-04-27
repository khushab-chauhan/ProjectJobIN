from django.db import models

# Create your models here.

class CAR(models.Model):
    CAR_MODEL = models.CharField(max_length=255,blank=False,null=False)
    CAR_MADE = models.CharField(max_length=255,blank=False,null=False)
    CAR_PRICE =  models.FloatField()