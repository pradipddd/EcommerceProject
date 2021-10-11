from django.shortcuts import redirect, render

from Accounts.models import Customer
from .models import Order_item
from Seller.models import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




def HomeView(request):
    template_name='Customer/Home.html'
    context={}
    return render(request,template_name,context)

# def Customermobileview(request):
#     mobile=Mobile.objects.all()
#     template_name='Customer/Customermobile.html'
#     context={'mobile':mobile}
#     return render(request,template_name,context)

# def Customerlaptopview(request):
#     laptop=Laptop.objects.all()
#     template_name='Customer/Customerlaptop.html'
#     context={'laptop':laptop}
#     return render(request,template_name,context)

# def Customergroceryview(request):
#     grocery=Grocery.objects.all()
#     template_name='Customer/Customergrocery.html'
#     context={'grocery':grocery}
#     return render(request,template_name,context)

@login_required(login_url='login')
def Laptopview(request,pk):
    # laptop=Laptop.objects.get(id=pk)
    # user=request.user
    # cst=Customer.objects.get(user=user)
    # x=Order_item.objects.get_or_create(customer=cst,laptop=laptop,mobile=None,grocery=None,price=laptop.price,quantity=1)
    # if x[1]==False:
    #     y=Order_item.objects.filter(customer=cst,laptop=laptop).first()
    #     z=y.quantity+1
    #     y.quantity=z
    #     p=y.price*y.quantity
    #     y.price=p
    #     y.save()
    # return redirect('cartview')
    laptop=Laptop.objects.get(id=pk)
    user=request.user
    try:
        cst=Customer.objects.get(user=user)
        y=Order_item.objects.filter(customer=cst,laptop=laptop).first()
        if y:
            z=y.quantity+1
            p=y.price/y.quantity
            q=p*z
            y.price=q
            y.quantity=z
            y.save()
            print('Updated!!!')
            return redirect('cartview')
        else:
            Order_item.objects.create(customer=cst,laptop=laptop,mobile=None,grocery=None,price=laptop.price,quantity=1)
            print('Created!!!')
        return redirect('cartview')
    except Customer.DoesNotExist:
        return redirect('login')

@login_required(login_url='login')
def Mobileview(request,pk):
    mobile=Mobile.objects.get(id=pk)
    user=request.user
    try:
        cst=Customer.objects.get(user=user)
        y=Order_item.objects.filter(customer=cst,mobile=mobile).first()
        if y:
            z=y.quantity+1
            p=y.price/y.quantity
            q=p*z
            y.price=q
            y.quantity=z
            y.save()
            print('Updated!!!')
            return redirect('cartview')
        else:
            Order_item.objects.create(customer=cst,laptop=None,mobile=mobile,grocery=None,price=mobile.price,quantity=1)
            print('Created!!!')
        return redirect('cartview')
    except Customer.DoesNotExist:
        return redirect('login')

@login_required(login_url='login')
def Groceryview(request,pk):
    grocery=Grocery.objects.get(id=pk)
    user=request.user
    try:
        cst=Customer.objects.get(user=user)
        y=Order_item.objects.filter(customer=cst,grocery=grocery).first()
        if y:
            z=y.quantity+1
            p=y.price/y.quantity
            q=p*z
            y.price=q
            y.quantity=z
            y.save()
            print('Updated!!!')
            return redirect('cartview')
        else:
            Order_item.objects.create(customer=cst,laptop=None,mobile=None,grocery=grocery,price=grocery.price,quantity=1)
            print('Created!!!')
        return redirect('cartview')
    except Customer.DoesNotExist:
        return redirect('login')

@login_required(login_url='login')
def Cartview(request):
    user=request.user
    try:
        cst=Customer.objects.get(user=user)
        ord=Order_item.objects.filter(customer=cst)
        price=0
        for i in ord:
            price=price+i.price
        print(len(ord))
        tord=len(ord)
        template_name='Customer/Cartview.html'
        context={'ord':ord,'tord':tord,'price':price}
        return render(request,template_name,context)
    except Customer.DoesNotExist:
        return redirect ('logout')

@login_required(login_url='login')
def Deleteitemview(request,pk):
    # item=Order_item.objects.get(id=pk)
    # item.delete()
    # return redirect('cartview')
    y=Order_item.objects.get(id=pk)
    if y.quantity>1:
        z=y.quantity-1
        p=y.price/y.quantity
        q=p*z
        y.price=q
        y.quantity=z
        y.save()
        print('Updated!!!')
        return redirect('cartview')
    else:
        print('Deleted!!')
        y.delete()
    return redirect('cartview')

def Updateallitemview(request,pk):
    y=Order_item.objects.filter(id=pk).first()
    if y:
        z=y.quantity+1
        p=y.price/y.quantity
        q=p*z
        y.price=q
        y.quantity=z
        y.save()
        print('Updated!!!')
        return redirect('cartview')

def Customerlaptopview (request):
    user_list = Laptop.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'Customer/Customerlaptop.html', { 'users': users })

def Customergroceryview (request):
    user_list = Grocery.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'Customer/Customergrocery.html', { 'users': users })


def Customermobileview (request):
    user_list = Mobile.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(user_list, 5)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)

    return render(request, 'Customer/Customermobile.html', { 'users': users })


