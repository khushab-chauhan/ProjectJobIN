from django.db import models
from apps.master.models import Baseclass
from apps.users.constant import *

# Create your models here.

class User(Baseclass):
    Account_type = models.CharField(max_length=255,choices=Account_type,blank=False,null=False)
    email = models.EmailField(max_length=255,unique=True,null=False,blank=False)
    password = models.CharField(max_length=255,blank=False,null=False)
    is_active = models.BooleanField(default=False)
    otp = models.CharField(max_length=10,default='123456')

    def save(self, *args,**kwargs):
        if self.Account_type.lower() == 'candidate':
            self.is_active = True

        super(User,self).save(*args,**kwargs)


