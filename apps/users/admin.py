from django.contrib import admin
from apps.users.models import User,UserPersonalInfo
from apps.dashboard.models import CRUD
# Register your models here.

admin.site.register(User)
admin.site.register(UserPersonalInfo)
admin.site.register(CRUD)
