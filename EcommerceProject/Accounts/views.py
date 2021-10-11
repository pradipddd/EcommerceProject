from django.contrib import messages
from django.shortcuts import redirect, render
from .models import CustomUser, Customer, Seller
from .forms import CustomerCreationForm,SellerCreationForm
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.core.mail import send_mail
import math, random

def RegisterView(request):
    form=CustomerCreationForm()
    if request.method == 'POST':
        form=CustomerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('emailverify')
    template_name='Accounts/Register.html'
    context={'form':form}
    return render(request,template_name,context)

def LoginView(request):
    try:
        if request.method == 'POST':
            no=request.POST.get('mobile')
            p=request.POST.get('password')
            cuser=CustomUser.objects.filter(mobile_no=no).first()
            print(cuser)
            if cuser:
                if cuser.is_active:
                    user=authenticate(username=no,password=p)
                    if user and user.is_customer:
                        login(request,user)
                        return redirect('customerhome')
                    else:
                        messages.error(request,'You entered invalid credintial for mobile no.,password or you may not registered as a customer!!')
                        return redirect('login')
                else:
                    messages.error(request,'Still you do not activate your account please activate it below!!')
                    return redirect('emailverify')
            else:
                messages.error(request,'your are not register user plz register')
                
        template_name='Accounts/Login.html'
        context={}
        return render(request,template_name,context)
    except Customer.DoesNotExist:
        return redirect('logout')


    
def ShowView(request):
    usr=Customer.objects.all()
    print(usr)
    tempalte_name='Accounts/Show.html'
    context={'user':usr}
    return render(request,tempalte_name,context)

def LogoutView(request):
    logout(request)
    return redirect('customerhome')


def SellerRegisterView(request):
    form=SellerCreationForm()
    if request.method == 'POST':
        form=SellerCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('selleremailverify')
    template_name='Accounts/SellerRegister.html'
    context={'form':form}
    return render(request,template_name,context)

def SellerLoginView(request):
    try:
        if request.method == 'POST':
            no=request.POST.get('mobile')
            p=request.POST.get('password')
            suser=CustomUser.objects.get(mobile_no=no)
            if suser:
                if suser.is_active:
                    user=authenticate(username=no,password=p)
                    if user and user.is_seller:
                        login(request,user)
                        return redirect('sellerhome')
                    else:
                        messages.error(request,'You entered invalid credintial for mobile no.,password or you may not registered as a Seller!!')
                        return redirect('sellerlogin')
                else:
                    messages.error(request,'Still you do not activate your account please activate it below!!')
                    return redirect('selleremailverify')
            else:
                messages.error(request,'your are not register plz register ')

        template_name='Accounts/SellerLogin.html'
        context={}
        return render(request,template_name,context)    
    except Seller.DoesNotExist:
        return redirect('sellerlogout')

    
def SellerShowView(request):
    usr=Seller.objects.all()
    print(usr)
    tempalte_name='Accounts/SellerShow.html'
    context={'user':usr}
    return render(request,tempalte_name,context)

def SellerLogoutView(request):
    logout(request)
    return redirect('sellerhome')

def generateOTP() :
     digits = "0123456789"
     OTP = ""
     for i in range(4) :
         OTP += digits[math.floor(random.random() * 10)]
     return OTP

def send_otp(request):
     email=request.POST.get("email")
     print(email)
     o=generateOTP()
     print(o)
     htmlgen = 'Your OTP is '+o
     send_mail('OTP request',htmlgen,'pradipdjango@gmail.com',[email], fail_silently=False)
     return HttpResponse(o)


def CustomerEmailVerificationview(request):
    template_name='Accounts/Customeremailverify.html'
    context={}
    return render(request,template_name,context)

def Customeractivateview(request):
    try:
        email=request.POST.get('email')
        customer=CustomUser.objects.get(email=email)
        customer.is_active=True
        customer.save()
        return render('login')
    except Customer.DoesNotExist:
        return redirect('logout')

def SellerEmailVerificationview(request):
    template_name='Accounts/Selleremailverify.html'
    context={}
    return render(request,template_name,context)

def Selleractivateview(request):
    try:
        email=request.POST.get('email')
        print(email)
        customer=CustomUser.objects.get(email=email)
        print(customer)
        customer.is_active=True
        print(customer.is_active)
        customer.save()
        return redirect('sellerlogin')
    except Seller.DoesNotExist:
        return redirect('sellerlogout')
