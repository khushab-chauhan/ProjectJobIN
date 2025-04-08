from django.urls import path
from apps.dashboard.views import *

urlpatterns = [
    path('',login,name='login'),
    path('dashboard/',dashboard,name='dashboard'),
    path('forgot/',forgot,name='forgot'),
    path('otp_varify/',otp_varify,name='otp_varify'),
    path('profile/',profile,name='profile'),
    path('register_otp/',register_otp,name='register_otp'),
    path('register/',register,name='register'),
]
