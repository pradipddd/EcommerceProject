from django.urls import path
from .views import LoginView, LogoutView, RegisterView, SellerLoginView, SellerLogoutView, SellerRegisterView, SellerShowView, ShowView, homeview



urlpatterns=[
    path('',homeview,name='home'),
    path('reg/',RegisterView,name='register'),
    path('log/',LoginView,name='login'),
    path('lout/',LogoutView,name='logout'),
    path('show/',ShowView,name='show'),
    path('sreg/',SellerRegisterView,name='sellerregister'),
    path('slog/',SellerLoginView,name='sellerlogin'),
    path('slout/',SellerLogoutView,name='sellerlogout'),
    path('sshow/',SellerShowView,name='sellershow'),
]