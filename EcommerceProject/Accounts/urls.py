from django.urls import path
from .views import CustomerEmailVerificationview, Customeractivateview, LoginView, LogoutView, RegisterView, SellerEmailVerificationview, SellerLoginView, SellerLogoutView, SellerRegisterView, SellerShowView, Selleractivateview, ShowView, send_otp



urlpatterns=[
    path('reg/',RegisterView,name='register'),
    path('log/',LoginView,name='login'),
    path('lout/',LogoutView,name='logout'),
    path('show/',ShowView,name='show'),
    path('sreg/',SellerRegisterView,name='sellerregister'),
    path('slog/',SellerLoginView,name='sellerlogin'),
    path('slout/',SellerLogoutView,name='sellerlogout'),
    path('sshow/',SellerShowView,name='sellershow'),
   path("send_otp/",send_otp,name="send otp"),
    path('',CustomerEmailVerificationview,name='emailverify'),
    path('activate/',Customeractivateview,name='Customeractivate'),
    path('email/',SellerEmailVerificationview,name='selleremailverify'),
    path('selleractivate/',Selleractivateview,name='Selleractivate')  
]