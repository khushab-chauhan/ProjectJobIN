from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from apps.master.utils.email_varify import email_varify
from apps.master.utils.password_varify import password_varify
from apps.master.utils.otp_generator import otp_generator
from apps.users.models import User
from functools import wraps
from django.contrib.auth.decorators import login_required
from .forms import CRUDforms
from django.contrib.auth import get_user
# Create your views here.

def login_requirement(my_fucn):
    @wraps(my_fucn)
    def _wrapped(request,*args,**kwargs):
        if 'user_id' not  in request.session:
            messages.error(request, 'You must be logged in to access this page.')
            return redirect('login')

        return my_fucn(request,*args,**kwargs)
    return _wrapped 


def youcannot_access(my_fucn):
    @wraps(my_fucn)
    def _wrapped(request,*args,**kwargs):
        if 'user_id' not  in request.session:
            messages.error(request, 'does not have page.')
            return redirect('login')

        return my_fucn(request,*args,**kwargs)
    return _wrapped 


def login(request):
    if request.method == 'POST':
        email_ = request.POST['email']
        password_ = request.POST['password']

        if not email_varify(email_):
            messages.error(request,"invalid email")
            return redirect('login') 
        
        if  not User.objects.filter(email = email_).exists():
            messages.error(request,"email does not exits")
            return redirect('login') 
        else:
            user = User.objects.get(email = email_)
            if password_ == user.password:
                request.session['user_id'] = str(user.id)
                print(request.session['user_id'])
                return redirect('dashboard') 
            else:
                messages.error(request, 'Invalid password')
                return redirect('login')




    return render(request,'dashboard/login.html')


def register(request):
    if request.method == 'POST':
        Account_type_ = request.POST['Account_type']
        email_ = request.POST['email']
        password_ = request.POST['password']
        confirm_password_ = request.POST['confirm_password']

        if not email_varify(email_):
            messages.error(request,"invalid email")
            return redirect('register')
        
        if not password_varify(password_)[0]:
            messages.error(request,password_varify(password_)[1])
            return redirect('register')

        if password_ != confirm_password_:
            messages.error(request,"password not match") 
            return redirect('register')
        
        if User.objects.filter(email = email_).exists():
            messages.error(request, 'Email already exists')
            return redirect('register')
        
        InnerQuerySet = User.objects.create(
            Account_type = Account_type_,
            email = email_,
            password = password_
        )
        InnerQuerySet.save()
        return redirect('login')
    return render(request,'dashboard/register.html')


def forgot(request):
    if request.method == 'POST':
        email_ = request.POST['email']

        if not email_varify(email_):
            messages.error(request,"invalid email")
            return redirect('forgot')
        
        if not User.objects.filter(email = email_).exists():
            messages.error(request, 'Email Does not match')
            return redirect('forgot')
        else:
            user = User.objects.get(email = email_)
            otp_ = otp_generator()
            subject = "SEND OTP OF REGISTER"
            message = f"""
    Dear {user.Account_type}
You have requested to reset your password. Please use the following OTP to reset your password: {otp_}

Regards,
JOBIN Team
            """
            recipient_list = [f'{email_}']

            send_mail(subject,message,settings.EMAIL_HOST_USER,recipient_list)    

            user.otp = otp_

            user.save()

            messages.success(request, "An OTP has been sent to your registered email. Please check your inbox.")
            return render(request, 'dashboard/otp_varify.html', {'email':email_})



    return render(request,'dashboard/forgot.html')

@youcannot_access
def otp_varify(request):
    print('here-1')
    if request.method == 'POST':
        email_ = request.POST['email']
        otp_ = request.POST['otp']
        password_ = request.POST['password']
        confirm_password_ = request.POST['confirm_password']

        if not email_varify(email_):
            messages.error(request, 'Invalid email')
            return render(request, 'dashboard/otp_varify.html', {'email':email_})
        
        if not User.objects.filter(email=email_).exists():
            messages.error(request, 'Email does not exist')
            return render(request, 'dashboard/otp_varify.html', {'email':email_})
        else:
            user = User.objects.get(email = email_)
            if user.otp == otp_:
                if password_ !=confirm_password_:
                    messages.error(request, 'Passwords do not match')
                    return render(request, 'dashboard/otp_varify.html', {'email':email_})
                
                if not password_varify(password_)[0]:
                    messages.error(request, password_varify(password_)[1])
                    return render(request, 'dashboard/otp_varify.html', {'email':email_})

                user.password = password_
                user.save()
                messages.success(request, "Password has been changed successfully")
                return redirect('login')
            else:
                messages.error(request, 'Invalid OTP')
                return render(request, 'dashboard/otp_varify.html', {'email':email_})

    return render(request,'dashboard/otp_varify.html')

@youcannot_access
def  logout(request):
    request.session.clear()
    messages.success(request,"Now, you are logged Out.")
    return redirect('login')

@login_requirement
def dashboard(request):
    return render(request,'dashboard/dashboard.html')

@login_requirement
def profile(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'user':user
    }
    return render(request,'dashboard/profile.html',context)


def register_otp(request):
    return render(request,'dashboard/register_otp.html')



# def crud(request):
#     form = CRUDforms()
#     if request.method == 'POST':
#         form = CRUDforms(request.POST, request.FILES)
#         if form.is_valid():
#             images_ = form.cleaned_data['images'],
#             full_name_ = form.cleaned_data['full_name'],
#             company_name_ = form.cleaned_data['company_name']
#             about_company_ = form.cleaned_data['about_company']
#             website_company_ = form.cleaned_data['website_company']
#             linkedin_company_ = form.cleaned_data['linkedin_company']
#             company_type_ = form.cleaned_data['company_type']
#             office_address_ = form.cleaned_data['office_address']
#             contact_phone = form.cleaned_data['contact_phone']
#      # Assign the logged-in user
#             form.save()                     # Now save to DB
#         else:
#             return redirect('crud')         # Redirect after success

    


#     return render(request,'dashboard/crud.html',{'form':form})
def crud(request):
    form = CRUDforms()
    if request.method == 'POST':
        form = CRUDforms(request.POST, request.FILES)
        if form.is_valid():
            crud = form.save(commit=False)
            crud.user = get_user(request)   # This fixes the SimpleLazyObject issue
            crud.save()
            return redirect('crud')
    return render(request, 'dashboard/crud.html', {'form': form})