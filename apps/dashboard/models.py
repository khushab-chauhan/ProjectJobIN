from django.db import models
from apps.master.models import Baseclass
from apps.dashboard.contants  import COMPANY_TYPE_CHOICE
import os
from apps.users.models import User
# Create your models here.

def user_profile_upload_path(instance , filename):
    ext = filename.split('.')[-1]
    filename = f'user_{instance.user.id}.{ext}'
    return os.path.join('users_profile/',filename)

class CRUD(Baseclass):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='personal_infomations')
    images = models.ImageField(upload_to='',blank=True,null=True,default='Default_Images/default.jpg')
    full_name = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    about_company = models.TextField(blank=True,null=True)
    website_company = models.URLField(blank=True,null=True)
    linkedin_company = models.URLField(blank=True,null=True)
    company_type  = models.CharField(max_length=110,choices=COMPANY_TYPE_CHOICE,default='Private')
    office_address = models.TextField(blank=True,null=True)
    contact_phone = models.CharField(max_length=15, blank=True, null=True)

