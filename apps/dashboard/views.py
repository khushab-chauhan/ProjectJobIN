from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request,'dashboard/login.html')
def register(request):
    return render(request,'dashboard/register.html')
def dashboard(request):
    return render(request,'dashboard/dashboard.html')
def forgot(request):
    return render(request,'dashboard/forgot.html')
def otp_varify(request):
    return render(request,'dashboard/otp_varify.html')
def profile(request):
    return render(request,'dashboard/profile.html')
def register_otp(request):
    return render(request,'dashboard/register_otp.html')
