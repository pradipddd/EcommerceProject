from django.shortcuts import render
import razorpay
from django.views.decorators.csrf import csrf_exempt

from Accounts.models import Customer
from Customer.models import Order_item



def CustomerRazorpayPayment(request):
    amount = 0
    user=request.user
    cst=Customer.objects.get(user=user)
    ord=Order_item.objects.filter(customer=cst)
    for i in ord:
        amount=amount+i.price
    amount=amount*100
    amount1=amount/100
    if request.method == "POST":
        name = request.POST.get('name')
        client = razorpay.Client(
auth=("rzp_test_E0TrRpVfHMc1l2", "JglS56dT94J1VWwZvbra6SSw"))
        payment = client.order.create({'amount': amount, 'currency': 'INR',
'payment_capture': '1'})

    return render(request, 'CustomerPayment/Placeorder.html',{'amount':amount,'customer':cst,'amount1':amount1})

@csrf_exempt
def CustomerRazorpayconfirm(request):
    return render(request, "CustomerPayment/Confirmorder.html")

