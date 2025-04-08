from django.db import models
from apps.master.models import Baseclass
from apps.users.constant import *
import os
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

def user_profile_upload_path(instance, filename):
    ext  = filename.split('.')[-1]
    filename = f'user_{instance.user.id}.{ext}'
    return os.path.join('users_profile/',filename)


class UserPersonalInfo(Baseclass):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='personal_info'
    )
    profile_picture = models.ImageField(upload_to=user_profile_upload_path, default='Default_Images/default.jpg')
    first_name = models.CharField(max_length=255, null=True, blank=True, default='')
    last_name = models.CharField(max_length=255, null=True, blank=True, default='')
    mobile = models.CharField(max_length=255, blank=True, null=True, default='')
    gender = models.CharField(max_length=255, choices=GENDER_CHOICES, default='other')
    date_of_birth = models.DateField(
        null=True,
        blank=True,
        default=None
    )
    address = models.TextField(max_length=255, null=True, blank=True)