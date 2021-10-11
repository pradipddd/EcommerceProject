from django.http.response import HttpResponse
from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from Accounts.views import *

# @login_required(login_url='sellerlogin')
# def ProductView(request):
#     form=ProductForm()
#     if request.method == 'POST':
#         form=ProductForm(request.POST)
#         if form.is_valid():
#             product=form.save(commit=False)
#             seller=Seller.objects.get(user=request.user)
#             product.seller=seller
#             product.save()
#             return HttpResponse('Product Category Created!!!......')
#     template_name='Seller/Sellerproduct.html'
#     context={'form':form}
#     return render(request,template_name,context)

@login_required(login_url='sellerlogin')
# @seller_required(login_url='sellerlogin')
def ProductView(request):
    form=ProductForm()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            product1=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            product=Product.objects.filter(seller=selleruser)
            prdlist=[]
            for prd in product:
                prdlist.append(prd.category_name)
            name=form.cleaned_data.get('category_name')
            if name in prdlist:
                messages.error(request,'That Category is already present')
            else:
                product1.seller=selleruser
                form.save()
                return redirect('sellerhome')
    template_name='Seller/Sellerproduct.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellerlaptopview(request):
    form=Laptopform()
    if request.method == 'POST':
        form=Laptopform(request.POST,request.FILES)
        if form.is_valid():
            laptop=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            product=Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name=='laptop':
                    laptop.product=prd
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellerlaptop.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellermobileview(request):
    form=Mobileform()
    if request.method == 'POST':

        form=Mobileform(request.POST,request.FILES)
        if form.is_valid():
            mobile=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            x=Product.objects.filter(seller=selleruser)
            for i in x:
                if i.category_name=='mobile':
                    mobile.product=i
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellermobile.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellergroceryview(request):
    form=Groceryform()
    if request.method == 'POST':
        form=Groceryform(request.POST,request.FILES)
        if form.is_valid():
            grocery=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            x=Product.objects.filter(seller=selleruser)
            for i in x:
                if i.category_name=='grocery':
                    grocery.product=i
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellergrocery.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellerinventoryview(request):
    selleruser=Seller.objects.get(user=request.user)
    product=Product.objects.filter(seller=selleruser)
    lap=None
    mob=None
    gro=None
    for prd in product:
        if prd.category_name=='laptop':
            lap=Laptop.objects.filter(product=prd)
        elif prd.category_name=='mobile':
            mob=Mobile.objects.filter(product=prd)
        elif prd.category_name=='grocery':
            gro=Grocery.objects.filter(product=prd)
    template_name='Seller/Sellerinventory.html'
    context={'lap':lap,'mob':mob,'gro':gro}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellerlaptopupdateview(request,lapupdate):
    lap=Laptop.objects.get(id=lapupdate)
    form=Laptopform(instance=lap)
    if request.method == 'POST':
        form=Laptopform(request.POST,request.FILES,instance=lap)
        if form.is_valid():
            laptop=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            product=Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name=='laptop':
                    laptop.product=prd
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellerlaptop.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')   
def Sellermobileupdateview(request,mobupdate):
    mob=Mobile.objects.get(id=mobupdate)
    form=Mobileform(instance=mob)
    if request.method == 'POST':
        form=Mobileform(request.POST,request.FILES,instance=mob)
        if form.is_valid():
            mobile=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            product=Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name=='mobile':
                    mobile.product=prd
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellermobile.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellergroceryupdateview(request,groupdate):
    gro=Grocery.objects.get(id=groupdate)
    form=Groceryform(instance=gro)
    if request.method == 'POST':
        form=Groceryform(request.POST,request.FILES,instance=gro)
        if form.is_valid():
            grocery=form.save(commit=False)
            selleruser=Seller.objects.get(user=request.user)
            product=Product.objects.filter(seller=selleruser)
            for prd in product:
                if prd.category_name=='grocery':
                    grocery.product=prd
                    form.save()
                    return redirect('sellerinventory')
    template_name='Seller/Sellergrocery.html'
    context={'form':form}
    return render(request,template_name,context)

@login_required(login_url='sellerlogin')
def Sellerlaptopdeleteview(request,lapdelete):
    lap=Laptop.objects.get(id=lapdelete)
    lap.delete()
    return redirect('sellerinventory')

@login_required(login_url='sellerlogin')
def Sellermobiledeleteview(request,mobdelete):
    mob=Mobile.objects.get(id=mobdelete)
    mob.delete()
    return redirect('sellerinventory')

@login_required(login_url='sellerlogin')
def Sellergrocerydeleteview(request,grodelete):
    gro=Grocery.objects.get(id=grodelete)
    gro.delete()
    return redirect('sellerinventory')

def Sellerhomeview(request):
    template_name='Seller/Sellerhome.html'
    context={}
    return render(request,template_name,context)
