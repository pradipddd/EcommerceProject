from django.urls import path
from .views import CustomerRazorpayPayment, CustomerRazorpayconfirm

urlpatterns = [
    path('customerpay/',CustomerRazorpayPayment, name='customerrazorpay'),
     path('customersuccess/' ,CustomerRazorpayconfirm, name='customerrazorpaysuccess')
]